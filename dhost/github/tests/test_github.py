from unittest import TestCase, mock

from dhost.github.github import GithubAPI


class GithubAPITestCase(TestCase):

    def setUp(self):
        self.g = GithubAPI(token='github_token')

    def test_get_token(self):
        self.assertEqual(self.g.get_token(), 'github_token')

    def test__get_authorization_header(self):
        authorization_header = self.g._get_authorization_header()
        self.assertEqual(authorization_header,
                         {'Authorization': 'token github_token'})

    def test_get_headers(self):
        headers = self.g.get_headers()
        self.assertIsNotNone(headers['Accept'])
        self.assertIsNotNone(headers['Authorization'])

    def test_get_headers_additionnal_headers(self):
        headers = self.g.get_headers({'Add': 'additionnal_headers'})
        self.assertIsNotNone(headers['Add'])

    def test__prepare_request(self):
        url, headers = self.g._prepare_request(url='/test_url')
        self.assertIsNotNone(headers['Accept'])
        self.assertIsNotNone(headers['Authorization'])
        self.assertEqual(url, 'https://api.github.com/test_url')

    def test__request_error(self):
        pass

    def test_get(self):
        pass

    def test_post(self):
        pass

    def test_patch(self):
        pass

    def test_head(self):
        pass

    def test_delete(self):
        pass

    def test_get_scopes(self):
        pass

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_get_user(self, mock):
        self.g.get_user(username='octocat')
        mock.assert_called_once_with('/users/octocat')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_list_repos(self, mock):
        self.g.list_repos()
        mock.assert_called_once_with('/user/repos')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_get_repo(self, mock):
        self.g.get_repo(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_list_branches(self, mock):
        self.g.list_branches(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World/branches')

    def test_download_repo(self):
        pass

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_list_hooks(self, mock):
        self.g.list_hooks(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_get_hook(self, mock):
        self.g.get_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_get_hook_config(self, mock):
        self.g.get_hook_config(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with(
            '/repos/octocat/Hello-World/hooks/1/config')

    @mock.patch('dhost.github.github.GithubAPI.post')
    def test_create_hook(self, mock):
        self.g.create_hook(owner='octocat',
                           repo='Hello-World',
                           webhook_url='webhook_test_url')
        mock.assert_called_once_with(
            '/repos/octocat/Hello-World/hooks', {
                'name': 'web',
                'config': {
                    'url': 'webhook_test_url',
                    'insecure_ssl': False,
                },
            })

    @mock.patch('dhost.github.github.GithubAPI.patch')
    def test_update_hook(self, mock):
        self.g.update_hook(owner='octocat',
                           repo='Hello-World',
                           hook_id=1,
                           data='test_data')
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1',
                                     'test_data')

    @mock.patch('dhost.github.github.GithubAPI.patch')
    def test_update_hook_config(self, mock):
        self.g.update_hook_config(owner='octocat',
                                  repo='Hello-World',
                                  hook_id=1,
                                  data='test_data')
        mock.assert_called_once_with(
            '/repos/octocat/Hello-World/hooks/1/config', 'test_data')

    @mock.patch('dhost.github.github.GithubAPI.delete')
    def test_delete_hook(self, mock):
        self.g.delete_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1')

    @mock.patch('dhost.github.github.GithubAPI.get')
    def test_ping_hook(self, mock):
        self.g.ping_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1/pings',
                                     code=204)
