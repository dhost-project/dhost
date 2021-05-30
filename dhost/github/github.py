# https://docs.github.com/en/developers/apps/scopes-for-oauth-apps#available-scopes
import requests

from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):
    def __init__(self, message="Github account linked."):
        super().__init__(message)


class GithubAPI:
    """A github REST API wrapper"""
    TOKEN_NAME = 'token'

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
        token_name = self.TOKEN_NAME
        return {'Authorization': '{} {}'.format(token_name, token)}

    def _get_headers(self):
        headers = {'Accept': 'application/vnd.github.v3+json'}
        headers.update(self._get_authorization_header())
        return headers

    def get_headers(self):
        return self._get_headers()

    def get(self, url, headers=None, *args, **kwargs):
        if headers is None:
            headers = self.get_headers()
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == 200:
            return r.json()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}'.format(
                    url, r.status_code))

    def request_private_repo_access(self):
        """Request access to public and private repositories hooks.
        with the scope: `read:repo_hook`
        """
        pass

    def get_repos(self):
        """Return a list of accessible repositories from te current token"""
        github_repos_url = 'https://api.github.com/user/repos'
        return self.get(url=github_repos_url)

    def get_repo(self, repo_name: str):
        """Return a single repository"""
        github_repo_url = 'https://api.github.com/users/{}/repos/{}'
        url = github_repo_url.format(self.github_name, repo_name)
        return self.get(url=url)
