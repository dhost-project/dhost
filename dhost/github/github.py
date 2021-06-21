"""
A wrapper for the Github REST API with OAuth
"""
import requests
from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):

    def __init__(self, message="Github account not linked."):
        super().__init__(message)


class GithubAPI:
    """A github REST API wrapper."""
    GITHUB_API_URL = 'https://api.github.com'
    GITHUB_TOKEN_TYPE = 'token'
    GITHUB_WEBHOOK_URL = 'https://localhost:8000/github/webhook/'

    def __init__(self, token: str):
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
        headers.update(headers)
        return headers

    def get_headers(self, additionnal_headers=None):
        return self._get_headers(additionnal_headers)

    def _prepare_request(self, url=None, headers=None, full_url=None):
        url = full_url if full_url else self.GITHUB_API_URL + url
        headers = self.get_headers(additionnal_headers=headers)
        return url, headers

    def get(self, url, headers, code=200, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.get(url, headers=headers, *args, **kwargs)
        if r.status_code == code:
            return r.json()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def post(self, url, headers, data, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.post(url, headers=headers, data=data, *args, **kwargs)
        if r.status_code == 201:
            return r.json()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def patch(self, url, headers, data, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, full_url)
        r = requests.patch(url, headers=headers, data=data, *args, **kwargs)
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

    def delete(self, url, headers, full_url=None, *args, **kwargs):
        url, headers = self._prepare_request(url, headers, *args, **kwargs)
        r = requests.delete(url, headers=headers, *args, **kwargs)
        if r.status_code == 204:
            return r.json()
        else:
            raise Exception(
                'Error trying to delete `{}`, error code: {}, message: {}'.
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

    def list_repos(self):
        """Return a list of accessible repositories from the current token"""
        return self.get('/user/repos')

    def get_repo(self, owner, repo):
        """Return a single repository."""
        return self.get(f'/repos/{owner}/{repo}')

    def list_branches(self, owner, repo):
        return self.get(f'/repos/{owner}/{repo}/branches')

    def download_repo(self, owner, repo, ref):
        """Download a repository"""
        url, headers = self._prepare_request(
            f'/repos/{owner}/{repo}/tarball/{ref}')
        r = requests.get(url, headers=headers, allow_redirects=True)
        dhost_username = self.user.username
        if r.status_code == 200:
            with open(f'{dhost_username}_{owner}_{repo}.tar', 'wb') as source:
                source.write(r.content)
                source.close()
        else:
            raise Exception(
                'Error trying to access `{}`, error code: {}, message: {}'.
                format(url, r.status_code, r.content))

    def list_hooks(self, owner, repo):
        return self.get(f'/repos/{owner}/{repo}/hooks')

    def get_hook(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}')

    def get_hook_config(self, owner, repo, hook_id):
        return self.get(f'/repos/{owner}/{repo}/hooks/{hook_id}/config')

    def create_hook(self, owner, repo, active=True, name='web'):
        """Create a Github repository webhook."""
        active = active
        data = {
            'name': name,
            'config': {
                'url': self.GITHUB_WEBHOOK_URL,
                'insecure_ssl': False,
            }
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

    def __init__(self, github_social=None, user=None):
        if github_social:
            self.github_social = github_social
        else:
            self.github_social = self.get_social(user)
        self.github_name = self.get_github_name()
        self.token = self.get_token()

    @classmethod
    def get_social(cls, user):
        try:
            return user.social_auth.get(provider='github')
        except ObjectDoesNotExist:
            raise GithubNotLinkedError()

    def get_github_name(self):
        if 'login' not in self.github_social.extra_data:
            raise Exception(
                "'login' not present in github_social.extra_data for "
                "user '{}' (id: '{}')".format(self.github_social.user,
                                              self.github_social.user.id))
        return self.github_social.extra_data['login']

    def get_token(self):
        if 'access_token' not in self.github_social.extra_data:
            raise Exception(
                "'access_token' not present in github_social.extra_data for "
                "user '{}' (id: '{}')".format(self.github_social.user,
                                              self.github_social.user.id))
        return self.github_social.extra_data['access_token']
