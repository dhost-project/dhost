"""A wrapper for the Github REST API with OAuth."""
import logging
import os

import requests

from .utils import get_token_from_github_account, get_user_github_account

logger = logging.getLogger(__name__)


class GithubAPIError(Exception):
    """Raised if a status code was not expected."""

    pass


class GithubAPI:
    """A github REST API wrapper."""

    GITHUB_API_URL = 'https://api.github.com'
    GITHUB_TOKEN_TYPE = 'token'

    def __init__(self, token: str):
        # Github API token used to make requests
        self.token = token

    def get_token(self):
        return self.token

    def _get_authorization_header(self):
        token = self.get_token()
        token_type = self.GITHUB_TOKEN_TYPE
        return {'Authorization': '{} {}'.format(token_type, token)}

    def get_headers(self, additionnal_headers=None):
        headers = {'Accept': 'application/vnd.github.v3+json'}
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
        try:
            # try to get a message from the response if it exist
            response_json = response.json()
            if 'message' in response_json:
                content = response_json['message']
        except TypeError:
            content = response.content
        raise GithubAPIError(f'{url} ({response.status_code}) {content}')

    def get(self, url, headers=None, code=200, json=True, *args, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == code:
            if json:
                return r.json()
            else:
                return r
        self._request_error(response=r, url=url)

    def post(self, url, data, headers=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.post(url, headers=headers, data=data, *args, **kwargs)
        if r.status_code == 201:
            return r.json()
        self._request_error(response=r, url=url)

    def patch(self, url, data, headers=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.patch(url, headers=headers, data=data, *args, **kwargs)
        if r.status_code == 200:
            return r.json()
        self._request_error(response=r, url=url)

    def head(self, url, headers=None, *args, **kwargs):
        r = self.get(url=url, headers=headers, json=False, *args, **kwargs)
        return r.headers

    def delete(self, url, headers=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers)
        r = requests.delete(url, headers=headers, *args, **kwargs)
        if r.status_code == 204:
            return r.json()
        self._request_error(response=r, url=url)

    def get_scopes(self, username):
        """Return oauth scopes."""
        head = self.head(f'/users/{username}')
        scopes = head['X-OAuth-Scopes']
        return scopes

    def get_user(self, username):
        return self.get(f'/users/{username}')

    def list_repos(self):
        """Return a list of accessible repositories from the current token."""
        return self.get('/user/repos')

    def get_repo(self, owner, repo):
        """Return a single repository."""
        return self.get(f'/repos/{owner}/{repo}')

    def list_branches(self, owner, repo):
        return self.get(f'/repos/{owner}/{repo}/branches')

    def download_repo(self, owner, repo, ref, path, archive_name=None):
        """Download a repository archive."""
        r = self.get(f'/repos/{owner}/{repo}/tarball/{ref}',
                     json=False,
                     allow_redirects=True)

        archive_name = repo if archive_name is None else archive_name

        # The archive path is: /<path>/<repo>.tar
        tar_path = os.path.join(path, archive_name + '.tar')

        # Create the folder if it doesn't exists already
        if not os.path.exists(path):
            os.makedirs(path)

        # write to the archive file
        with open(tar_path, 'wb') as source:
            source.write(r.content)
            source.close()

        return tar_path

    def list_hooks(self, owner, repo):
        return self.get(f'/repos/{owner}/{repo}/hooks')

    def get_hook(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}')

    def get_hook_config(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}/config')

    def create_hook(self, owner, repo, webhook_url, active=True, name='web'):
        """Create a Github repository webhook."""
        data = {
            'name': name,
            'config': {
                'url': webhook_url,
                'insecure_ssl': False,
            },
        }
        return self.post(f'/repos/{owner}/{repo}/hooks', data)

    def update_hook(self, owner, repo, hook_id, data):
        return self.patch(f'/repos/{owner}/{repo}/hooks/{hook_id}', data)

    def update_hook_config(self, owner, repo, hook_id, data):
        return self.patch(f'/repos/{owner}/{repo}/hooks/{hook_id}/config', data)

    def delete_hook(self, owner, repo, hook_id):
        return self.delete(f'/repos/{owner}/{repo}/hooks/{hook_id}')

    def ping_hook(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}/pings',
                        code=204)


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
            message = '{}, user: {}'.format(str(e), self.user)
            logger.warning(message)
            raise e
