"""A wrapper for the Github REST API with OAuth."""
import logging
import os
import tarfile

import requests

from .utils import get_token_from_github_account, get_user_github_account

logger = logging.getLogger(__name__)


def untar_source(tar_file, target_path, delete_tarball=True):
    """Extract a Github repository tarball."""
    tar = tarfile.open(tar_file)
    folder_name = tar.getnames()[0]
    tar.extractall(target_path)
    tar.close()

    if delete_tarball:
        os.remove(tar_file)

    return str(os.path.join(target_path, folder_name))


class GithubAPIError(Exception):
    """Raised if a status code was not expected."""

    pass


class GithubAPI:
    """A Github REST API wrapper."""

    GITHUB_API_URL = "https://api.github.com"
    GITHUB_TOKEN_TYPE = "token"

    def __init__(self, token: str, fail_silently: bool = False):
        # Github API token used to make requests
        self.token = token
        self.fail_silently = fail_silently

    def get_token(self):
        return self.token

    def _get_authorization_header(self):
        token = self.get_token()
        token_type = self.GITHUB_TOKEN_TYPE
        return {"Authorization": "{} {}".format(token_type, token)}

    def get_headers(self, additionnal_headers=None):
        headers = {"Accept": "application/vnd.github.v3+json"}
        headers.update(self._get_authorization_header())
        if additionnal_headers:
            headers.update(additionnal_headers)
        return headers

    def _prepare_request(self, url, headers=None):
        url = self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
        return url, headers

    def _request_error(self, response, url):
        """Raise an exception if a status code was not expected."""
        if not self.fail_silently:
            import json

            try:
                # try to get a message from the response if it exist
                response_json = response.json()
                if "message" in response_json:
                    content = response_json["message"]
            except json.decoder.JSONDecodeError:
                content = response.content
            raise GithubAPIError(f"{url} ({response.status_code}) {content}")

    def get(self, url, headers=None, code=200, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.get(url, headers=headers, **kwargs)
        if r.status_code != code:
            self._request_error(response=r, url=url)
        return r

    def post(self, url, data, headers=None, code=201, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.post(url, headers=headers, data=data, **kwargs)
        if r.status_code != code:
            self._request_error(response=r, url=url)
        return r

    def patch(self, url, data, headers=None, code=200, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.patch(url, headers=headers, data=data, **kwargs)
        if r.status_code != code:
            self._request_error(response=r, url=url)
        return r

    def delete(self, url, headers=None, code=204, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.delete(url, headers=headers, **kwargs)
        if r.status_code != code:
            self._request_error(response=r, url=url)
        return r

    def head(self, url, headers=None, code=200, **kwargs):
        r = self.get(url=url, headers=headers, code=code, **kwargs)
        return r.headers

    def get_scopes(self, username):
        """Return oauth scopes."""
        head = self.head(f"/users/{username}")
        scopes = head["X-OAuth-Scopes"]
        return scopes

    def get_user(self, username):
        return self.get(f"/users/{username}").json()

    def list_repos(self):
        """Return a list of accessible repositories from the current token."""
        return self.get("/user/repos").json()

    def get_repo(self, owner, repo):
        """Return a single repository."""
        return self.get(f"/repos/{owner}/{repo}").json()

    def list_branches(self, owner, repo):
        return self.get(f"/repos/{owner}/{repo}/branches").json()

    def download_repo_tar(self, owner, repo, ref, path, archive_name=None):
        """Download a repository archive."""
        r = self.get(
            f"/repos/{owner}/{repo}/tarball/{ref}",
            allow_redirects=True,
        )
        archive_name = repo if archive_name is None else archive_name

        # The archive path is: /<path>/<repo>.tar
        tar_file = os.path.join(path, archive_name + ".tar")

        # Create the folder if it doesn't exists already
        if not os.path.exists(path):
            os.makedirs(path)

        # write to the archive file
        with open(tar_file, "wb") as source:
            source.write(r.content)
            source.close()

        return tar_file

    def download_repo(
        self, owner, repo, ref, path, archive_name=None, delete_tarball=True
    ):
        """Download a repository, untar it and delete the tarball."""
        tar_file = self.download_repo_tar(
            owner=owner,
            repo=repo,
            ref=ref,
            path=path,
            archive_name=archive_name,
        )
        source_folder = untar_source(
            tar_file=tar_file,
            target_path=path,
            delete_tarball=delete_tarball,
        )
        return source_folder

    def list_hooks(self, owner, repo):
        return self.get(f"/repos/{owner}/{repo}/hooks").json()

    def get_hook(self, owner, repo, hook_id):
        return self.get(f"/repos/{owner}/{repo}/hooks/{hook_id}").json()

    def get_hook_config(self, owner, repo, hook_id):
        return self.get(f"/repos/{owner}/{repo}/hooks/{hook_id}/config").json()

    def create_hook(self, owner, repo, webhook_url, active=True, name="web"):
        """Create a Github repository webhook."""
        data = {
            "name": name,
            "config": {
                "url": webhook_url,
                "insecure_ssl": False,
            },
        }
        return self.post(f"/repos/{owner}/{repo}/hooks", data=data).json()

    def update_hook(self, owner, repo, hook_id, data):
        return self.patch(f"/repos/{owner}/{repo}/hooks/{hook_id}", data).json()

    def update_hook_config(self, owner, repo, hook_id, data):
        return self.patch(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/config", data
        ).json()

    def delete_hook(self, owner, repo, hook_id):
        return self.delete(f"/repos/{owner}/{repo}/hooks/{hook_id}").json()

    def ping_hook(self, owner, repo, hook_id):
        return self.get(
            f"/repos/{owner}/{repo}/hooks/{hook_id}/pings", code=204
        ).json()


class DjangoGithubAPI(GithubAPI):
    """Get the token from Django social auth."""

    def __init__(self, user):
        self.user = user

        # `get_user_github_account` will raise an exception if the user has no
        # github account linked, you should always ensure that when calling
        # this class you either catch exceptions or only call it if you know
        # that the user has a linked account (use `user_has_github_account`).
        self.github_account = get_user_github_account(self.user)

        # we can now get the token from the github_account
        token = get_token_from_github_account(self.github_account)

        super().__init__(token=token)

    def _request_error(self, *args, **kwargs):
        """Log exceptions."""
        try:
            super()._request_error(*args, **kwargs)
        except GithubAPIError as e:
            message = "{}, user: {}".format(str(e), self.user)
            logger.warning(message)
            raise e
