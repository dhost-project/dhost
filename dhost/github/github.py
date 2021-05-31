"""
A wrapper for the Github REST API with OAuth
"""
import requests
from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):

    def __init__(self, message="Github account linked."):
        super().__init__(message)


class GithubAPI:
    """A github REST API wrapper"""
    GITHUB_API_URL = 'https://api.github.com'
    TOKEN_TYPE = 'token'

    def __init__(self, user):
        self.user = user
        self.social = None
        self.token = None
        self.github_name = None

        self._get_social()
        self._get_token()

    def _get_social(self):
        try:
            self.social = self.user.social_auth.get(provider='github')
        except ObjectDoesNotExist:
            raise GithubNotLinkedError()
        else:
            self.github_name = self.social.extra_data['login']
            return self.social

    def _get_token(self):
        if self.social is not None:
            self.token = self.social.extra_data['access_token']
            return self.token
        else:
            raise Exception("Social is not set, call `_get_social` first.")

    def _get_authorization_header(self):
        token = self.token
        token_type = self.TOKEN_TYPE
        return {'Authorization': '{} {}'.format(token_type, token)}

    def _get_headers(self, additionnal_headers):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        headers.update(self._get_authorization_header())
        headers.update(headers)
        return headers

    def get_headers(self, additionnal_headers):
        return self._get_headers(additionnal_headers)

    def get(self, url=None, headers=None, full_url=None, *args, **kwargs):
        url = full_url if full_url else self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def head(self, url=None, headers=None, full_url=None, *args, **kwargs):
        url = full_url if full_url else self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
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
        check_scopes = f'/users/{username}'
        head = self.head(check_scopes)
        scopes = head['X-OAuth-Scopes']
        return scopes

    def get_user(self):
        username = self.github_name
        user_url = f'/users/{username}'
        return self.get(user_url)

    def get_repos(self):
        """Return a list of accessible repositories from the current token"""
        list_repo = '/user/repos'
        return self.get(list_repo)

    def get_repo(self, repo: str, owner: str = None):
        """Return a single repository"""
        owner = owner if owner else self.github_name
        repo_details = f'/users/{owner}/repos/{repo}'
        return self.get(repo_details)
