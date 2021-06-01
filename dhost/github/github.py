"""
A wrapper for the Github REST API with OAuth
"""
import requests
from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):

    def __init__(self, message="Github account not linked."):
        super().__init__(message)


class GithubAPI:
    """A github REST API wrapper"""
    GITHUB_API_URL = 'https://api.github.com'
    TOKEN_TYPE = 'token'

    def __init__(self, token: str):
        self.token = token

    def get_token(self):
        return self.token

    def _get_authorization_header(self):
        token = self.get_token()
        token_type = self.TOKEN_TYPE
        return {'Authorization': '{} {}'.format(token_type, token)}

    def _get_headers(self, additionnal_headers=None):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        headers.update(self._get_authorization_header())
        headers.update(headers)
        return headers

    def get_headers(self, additionnal_headers=None):
        return self._get_headers(additionnal_headers)

    def _prepare_request(self, url=None, headers=None, full_url=None):
        url = full_url if full_url else self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
        return url, headers

    def get(self, url=None, headers=None, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def head(self, url=None, headers=None, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.head(url, headers=headers, *args, **kwargs)
        if r.status_code == 200:
            return r.headers
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def request_private_repo_access(self):
        """Request access to public and private repositories hooks.
        with the scope: `read:repo_hook`
        """
        pass

    def get_scopes(self):
        """Return oauth scopes"""
        username = self.github_name
        head = self.head(f'/users/{username}')
        scopes = head['X-OAuth-Scopes']
        return scopes

    def get_user(self):
        username = self.github_name
        return self.get(f'/users/{username}')

    def get_repos(self):
        """Return a list of accessible repositories from the current token"""
        return self.get('/user/repos')

    def get_repo(self, repo: str, owner: str = None):
        """Return a single repository"""
        owner = owner if owner else self.github_name
        return self.get(f'/repos/{owner}/{repo}')

    def download_repo(self, repo: str, owner: str = None, ref: str = ''):
        """Download a repository"""
        owner = owner if owner else self.github_name
        dhost_username = self.user.username
        url, headers = self._prepare_request(
            f'/repos/{owner}/{repo}/tarball/{ref}')
        r = requests.get(url, headers=headers, allow_redirects=True)
        if r.status_code == 200:
            with open(f'{dhost_username}_{owner}_{repo}.tar', 'wb') as source:
                source.write(r.content)
                source.close()
            return 'Repository successfully downloaded.'
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))


class DjangoGithubAPI(GithubAPI):
    """Get the token from Django social auth"""

    def __init__(self, user):
        """
        :user: django user object
        """
        self.user = user
        self.social = self.get_social()
        self.github_name = self.get_github_name()
        self.token = self.get_token()

    def get_social(self):
        try:
            return self.user.social_auth.get(provider='github')
        except ObjectDoesNotExist:
            raise GithubNotLinkedError()

    def get_github_name(self):
        return self.get_social().extra_data['login']

    def get_token(self):
        return self.get_social().extra_data['access_token']
