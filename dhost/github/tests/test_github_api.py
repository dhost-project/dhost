import os
from unittest import TestCase, mock

from django.conf import settings

from dhost.github.github_api import GithubAPI, GithubAPIError

TMP_PATH = settings.TEST_DIR


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

    def test_get_headers_with_additionnal_headers(self):
        headers = self.g.get_headers({'Add': 'additionnal_headers'})
        self.assertIsNotNone(headers['Add'])

    def test__prepare_request(self):
        url, headers = self.g._prepare_request(url='/test_url')
        self.assertIsNotNone(headers['Accept'])
        self.assertIsNotNone(headers['Authorization'])
        self.assertEqual(url, 'https://api.github.com/test_url')

    @mock.patch('requests.get')
    def test_get(self, mock_get):
        mock_get.return_value = mock.Mock(status_code=200, json=lambda: {})
        self.g.get('/test')
        mock_get.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            })

    @mock.patch('requests.get')
    def test_get_404_status(self, mock_get):
        mock_get.return_value = mock.Mock(status_code=404, json=lambda:
                                          {'message': 'Not Found'})
        with self.assertRaises(GithubAPIError) as context:
            self.g.get('/test')
        self.assertIn('https://api.github.com/test (404) Not Found',
                      str(context.exception))

    @mock.patch('requests.get')
    def test_get_no_json(self, mock_get):
        mock_get.return_value = mock.Mock(status_code=200)
        self.g.get('/test', json=False)
        mock_get.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            })

    @mock.patch('requests.post')
    def test_post(self, mock_post):
        mock_post.return_value = mock.Mock(status_code=201, json=lambda: {})
        self.g.post('/test', data={'test_data': 'test'})
        mock_post.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            },
            data={'test_data': 'test'})

    @mock.patch('requests.post')
    def test_post_404_status(self, mock_post):
        mock_post.return_value = mock.Mock(status_code=404, content='test')
        with self.assertRaises(GithubAPIError) as context:
            self.g.post('/test', data={'test_data': 'test'})
        self.assertIn('https://api.github.com/test (404)',
                      str(context.exception))

    @mock.patch('requests.patch')
    def test_patch(self, mock_patch):
        mock_patch.return_value = mock.Mock(status_code=200, json=lambda: {})
        self.g.patch('/test', data={'test_data': 'test'})
        mock_patch.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            },
            data={'test_data': 'test'})

    @mock.patch('requests.patch')
    def test_patch_404_status(self, mock_patch):
        mock_patch.return_value = mock.Mock(status_code=404, content='test')
        with self.assertRaises(GithubAPIError) as context:
            self.g.patch('/test', data={'test_data': 'test'})
        self.assertIn('https://api.github.com/test (404)',
                      str(context.exception))

    @mock.patch('requests.get')
    def test_head(self, mock_get):
        mock_get.return_value = mock.Mock(status_code=200,
                                          headers={'test_head': 'test'})
        self.g.head('/test')
        mock_get.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            },
        )

    @mock.patch('requests.delete')
    def test_delete(self, mock_delete):
        mock_delete.return_value = mock.Mock(status_code=204, json=lambda: {})
        self.g.delete('/test')
        mock_delete.assert_called_once_with(
            'https://api.github.com/test',
            headers={
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token github_token'
            },
        )

    @mock.patch('requests.delete')
    def test_delete_404_status(self, mock_delete):
        mock_delete.return_value = mock.Mock(status_code=404, content='test')
        with self.assertRaises(GithubAPIError) as context:
            self.g.delete('/test')
        self.assertIn('https://api.github.com/test (404)',
                      str(context.exception))

    @mock.patch(
        'dhost.github.github_api.GithubAPI.head',
        mock.MagicMock(return_value={'X-OAuth-Scopes': 'oauth_test_scope'}))
    def test_get_scopes(self):
        oauth_scopes = self.g.get_scopes('octocat')
        self.assertEqual(oauth_scopes, 'oauth_test_scope')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_get_user(self, mock):
        self.g.get_user(username='octocat')
        mock.assert_called_once_with('/users/octocat')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_list_repos(self, mock):
        self.g.list_repos()
        mock.assert_called_once_with('/user/repos')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_get_repo(self, mock):
        self.g.get_repo(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_list_branches(self, mock):
        self.g.list_branches(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World/branches')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_download_repo(self, mock_get):
        mock_get.return_value = mock.Mock(content=b'data_test')
        self.g.download_repo(owner='octocat',
                             repo='Hello-World',
                             ref='master',
                             path=os.path.join(TMP_PATH, 'repos'))
        self.assertTrue(os.path.exists(TMP_PATH + '/repos/Hello-World.tar'))
        mock_get.assert_called_once_with(
            '/repos/octocat/Hello-World/tarball/master',
            json=False,
            allow_redirects=True)

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_download_repo_with_archive_name(self, mock_get):
        mock_get.return_value = mock.Mock(content=b'data_test')
        self.g.download_repo(owner='octocat',
                             repo='Hello-World',
                             ref='master',
                             path=os.path.join(TMP_PATH, 'repos'),
                             archive_name='foo_bar')
        self.assertTrue(os.path.exists(TMP_PATH + '/repos/foo_bar.tar'))

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_list_hooks(self, mock):
        self.g.list_hooks(owner='octocat', repo='Hello-World')
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_get_hook(self, mock):
        self.g.get_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_get_hook_config(self, mock):
        self.g.get_hook_config(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with(
            '/repos/octocat/Hello-World/hooks/1/config')

    @mock.patch('dhost.github.github_api.GithubAPI.post')
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

    @mock.patch('dhost.github.github_api.GithubAPI.patch')
    def test_update_hook(self, mock):
        self.g.update_hook(owner='octocat',
                           repo='Hello-World',
                           hook_id=1,
                           data='test_data')
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1',
                                     'test_data')

    @mock.patch('dhost.github.github_api.GithubAPI.patch')
    def test_update_hook_config(self, mock):
        self.g.update_hook_config(owner='octocat',
                                  repo='Hello-World',
                                  hook_id=1,
                                  data='test_data')
        mock.assert_called_once_with(
            '/repos/octocat/Hello-World/hooks/1/config', 'test_data')

    @mock.patch('dhost.github.github_api.GithubAPI.delete')
    def test_delete_hook(self, mock):
        self.g.delete_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1')

    @mock.patch('dhost.github.github_api.GithubAPI.get')
    def test_ping_hook(self, mock):
        self.g.ping_hook(owner='octocat', repo='Hello-World', hook_id=1)
        mock.assert_called_once_with('/repos/octocat/Hello-World/hooks/1/pings',
                                     code=204)
