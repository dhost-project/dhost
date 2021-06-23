"""
A wrapper for the Github REST API with OAuth
"""
import requests

from .utils import get_token_from_github_account, get_user_github_account


class GithubAPI:
    """A github REST API wrapper."""

    GITHUB_API_URL = 'https://api.github.com'
    GITHUB_TOKEN_TYPE = 'token'
    GITHUB_WEBHOOK_URL = 'https://localhost:8000/github/webhook/'

    def __init__(self, token: str):
        """
        The Github API token used to make requests.
        """
        self.token = token

    def get_token(self):
        return self.token

    def _get_authorization_header(self):
        token = self.get_token()
        token_type = self.GITHUB_TOKEN_TYPE
        return {'Authorization': '{} {}'.format(token_type, token)}

    def _get_headers(self, additionnal_headers=None):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        headers.update(self._get_authorization_header())
        headers.update(additionnal_headers)
        return headers

    def get_headers(self, additionnal_headers=None):
        return self._get_headers(additionnal_headers)

    def _prepare_request(self, url=None, headers=None, full_url=None):
        url = full_url if full_url else self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
        return url, headers

    def _request_error(self, response, expected_code, url=None):
        """Raise an exception if a status code was not expected."""
        raise Exception(
            'Error trying to access `{url}`, error code: {error_code} '
            '(expected code: {expected_code}), message: {content}'.format(
                url=url,
                error_code=response.status_code,
                expected_code=expected_code,
                content=response.content,
            ))

    def get(self, url, headers=None, code=200, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == code:
            return r.json()
        self._request_error(response=r, expected_code=code, url=url)

    def post(self, url, data, headers=None, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.post(url, headers=headers, data=data, *args, **kwargs)
        if r.status_code == 201:
            return r.json()
        self._request_error(response=r, expected_code=201, url=url)

    def patch(self, url, data, headers=None, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.patch(url, headers=headers, data=data, *args, **kwargs)
        if r.status_code == 200:
            return r.json()
        self._request_error(response=r, expected_code=200, url=url)

    def head(self, url=None, headers=None, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.head(url, headers=headers, *args, **kwargs)
        if r.status_code == 200:
            return r.headers
        self._request_error(response=r, expected_code=200, url=url)

    def delete(self, url, headers, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, *args, **kwargs)
        r = requests.delete(url, headers=headers, *args, **kwargs)
        if r.status_code == 204:
            return r.json()
        self._request_error(response=r, expected_code=204, url=url)

    def request_private_repo_access(self):
        """Request access to public and private repositories hooks.
        with the scope: `read:repo_hook`.
        """
        pass

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

    def download_repo(self, owner, repo, ref, path):
        """Download a repository archive."""
        url, headers = self._prepare_request(
            f'/repos/{owner}/{repo}/tarball/{ref}')
        r = requests.get(url, headers=headers, allow_redirects=True)
        if r.status_code == 200:
            tar_path = f'{owner}_{repo}.tar'
            with open(tar_path, 'wb') as source:
                source.write(r.content)
                source.close()
            return tar_path
        self._request_error(response=r, expected_code=200, url=url)

    def list_hooks(self, owner, repo):
        return self.get(f'/repos/{owner}/{repo}/hooks')

    def get_hook(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}')

    def get_hook_config(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}/config')

    def create_hook(self, owner, repo, active=True, name='web'):
        """Create a Github repository webhook."""
        data = {
            'name': name,
            'config': {
                'url': self.GITHUB_WEBHOOK_URL,
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
