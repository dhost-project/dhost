from unittest import mock

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from dhost.github.models import Branch, Repository, Webhook

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class RepositoryTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.u2 = User.objects.create(username='tom', password='tom')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={
                'access_token': 'token123',
                'login': 'john'
            },
        )
        self.repo1 = Repository.objects.create(
            id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.repo1.users.add(self.u1)
        self.repo_json = {
            "id": 191538244,
            "name": "MineSweeper",
            "owner": {
                "login": "2O4",
            },
            "size": 42,
        }

    def test_str(self):
        """
        Test Github's `__str__` function
        """
        github_str = str(self.repo1)
        self.assertEqual(str, type(github_str))

    def test_remove_user(self):
        self.repo1.remove_user(self.u1)
        self.assertFalse(self.repo1.users.filter(id=self.u1.id))

    def test_create_from_json(self):
        repo_json = self.repo_json
        repo = Repository.objects.create_from_json(repo_json=repo_json,
                                                   user=self.u1)
        self.assertEqual(2, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        self.assertTrue(repo.users.filter(id=self.u1.id).exists())
        self.assertTrue(Repository.objects.get(id=191538244))

    def test_update_or_create_from_json_exist(self):
        # if the repo already exist (same id)
        repo_json = self.repo_json
        repo_json.update({'id': 1})
        repo = Repository.objects.update_or_create_from_json(
            repo_json=repo_json, user=self.u2)
        self.assertEqual(1, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        # The Github repo exist but the user wasn't in it, we are testing that
        # they are added has well
        self.assertTrue(repo.users.filter(id=self.u2.id).exists())

    def test_update_or_create_from_json_doesnt_exist(self):
        repo_json = self.repo_json
        repo = Repository.objects.update_or_create_from_json(
            repo_json=repo_json, user=self.u1)
        self.assertEqual(2, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        self.assertTrue(repo.users.filter(id=self.u1.id).exists())

    @mock.patch(
        'dhost.github.github.DjangoGithubAPI.list_repos',
        mock.MagicMock(return_value=[
            {
                "id": 1,
                "name": "repo_1",
                "owner": {
                    "login": "dhost-project",
                },
                "size": 100,
            },
            {
                "id": 2,
                "name": "repo_2",
                "owner": {
                    "login": "dhost-project",
                },
                "size": 100,
            },
            {
                "id": 3,
                "name": "repo_3",
                "owner": {
                    "login": "dhost-project",
                },
                "size": 100,
            },
        ]),
    )
    def test_fetch_all(self):
        Repository.objects.fetch_all(self.u1)
        # 3 because 1 already exist, and 3 are added but one has the same ID
        # as an already existing repo so it will be updated instead.
        self.assertEqual(3, Repository.objects.count())
        # test that the repo wich already existed was updated
        self.assertEqual(Repository.objects.get(id=1).github_repo, "repo_1")
        # test that the new repo was added
        self.assertEqual(Repository.objects.get(id=3).github_repo, "repo_3")

    @mock.patch(
        'dhost.github.github.DjangoGithubAPI.get_repo',
        mock.MagicMock(
            return_value={
                "id": 1,
                "name": "dhost-front",
                "owner": {
                    "login": "dhost-project",
                },
                "size": 100,
            }),
    )
    def test_fetch_repo(self):
        self.repo1.fetch_repo(user=self.u1)
        self.assertEqual(self.repo1.extra_data['size'], 100)

    @mock.patch(
        'dhost.github.github.DjangoGithubAPI.get_repo',
        mock.MagicMock(
            return_value={
                "id": 222222,
                "name": "dhost-front",
                "owner": {
                    "login": "dhost-project",
                },
                "size": 100,
            }),
    )
    def test_fetch_repo_wrong_id(self):
        # If the Github ID doesn't match the local ID we shouldn't update the
        # object with the new data.
        with self.assertRaisesMessage(Exception, "The Github ID changed."):
            self.repo1.fetch_repo(user=self.u1)
            self.assertNotEqual(self.repo1.extra_data['size'], 100)

    def test_update_from_json_same_id(self):
        repo_json = {
            "id": 1,
            "name": "dhost-renamed",
            "owner": {
                "login": "dhost-project",
            },
            "size": 100,
        }
        self.repo1.update_from_json(repo_json)
        self.assertEqual(self.repo1.github_repo, 'dhost-renamed')

    def test_update_from_json_wrong_id(self):
        repo_json = {
            "id": 191538244,
            "name": "dhost-renamed",
            "owner": {
                "login": "dhost-project",
            },
            "size": 100,
        }
        with self.assertRaisesMessage(Exception, "The Github ID changed."):
            self.repo1.update_from_json(repo_json)
            self.assertNotEqual(self.repo1.extra_data['size'], 100)

    @mock.patch('dhost.github.github.DjangoGithubAPI.download_repo',
                mock.MagicMock(return_value='repo_example.tar'))
    def test_download_repo(self):
        self.repo1.download(user=self.u1,
                            ref='master',
                            path=settings.TEST_MEDIA_ROOT)

    @mock.patch('dhost.github.managers.BranchManager.fetch_repo_branches')
    def test_fetch_branches(self, mock):
        self.repo1.fetch_branches(self.u1)
        mock.assert_called_once_with(self.repo1, self.u1)

    @mock.patch('dhost.github.managers.WebhookManager.create_webhook')
    def test_create_webhook(self, mock):
        mock.return_value = 'webhook1'
        webhook = self.repo1.create_webhook(name='test_name')
        mock.assert_called_once_with(name='test_name', repo=self.repo1.id)
        self.assertEqual(webhook, 'webhook1')


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class BranchTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={'access_token': 'token123'},
        )
        self.repo1 = Repository.objects.create(
            id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.repo1.users.add(self.u1)
        self.branch1 = Branch.objects.create(
            repo=self.repo1,
            name='master',
            extra_data={'name': 'master'},
        )
        self.branch_json = {
            "name": "master",
            "commit": {
                "sha": "c5b97d5ae6c19d5c5df71a34c7fbeeda2479ccbc",
                "url": "",
            },
            "protected": True,
            "protection": {
                "required_status_checks": {
                    "enforcement_level": "non_admins",
                    "contexts": ["ci-test", "linter"],
                }
            },
            "protection_url": "",
        }

    def test_create_from_json(self):
        branch_json = self.branch_json
        branch = Branch.objects.create_from_json(repo=self.repo1,
                                                 branch_json=branch_json)
        self.assertEqual(2, Branch.objects.count())
        self.assertEqual(branch.name, 'master')
        self.assertEqual(branch.extra_data, branch_json)

    def test_update_or_create_from_json_exist(self):
        branch_json = self.branch_json
        branch = Branch.objects.update_or_create_from_json(
            repo=self.repo1, branch_json=branch_json)
        self.assertEqual(1, Branch.objects.count())
        self.assertEqual(branch.name, 'master')
        self.assertEqual(branch.extra_data, branch_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        branch_json = self.branch_json
        branch_json.update({'name': 'dev'})
        branch = Branch.objects.update_or_create_from_json(
            repo=self.repo1, branch_json=branch_json)
        self.assertEqual(2, Branch.objects.count())
        self.assertEqual(branch.name, 'dev')
        self.assertEqual(branch.extra_data, branch_json)


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class WebhookTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={'access_token': 'token123'},
        )
        self.repo1 = Repository.objects.create(
            id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.repo1.users.add(self.u1)
        self.webhook1 = Webhook.objects.create(repo=self.repo1, id=1)
        self.webhook_json = {
            "type": "Repository",
            "id": 12345678,
            "name": "web",
            "active": True,
            "events": ["push", "pull_request"],
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "https://example.com/webhook",
            },
            "updated_at": "2019-06-03T00:57:16Z",
            "created_at": "2019-06-03T00:57:16Z",
            "url": "",
            "test_url": "",
            "ping_url": "",
            "last_response": {
                "code": None,
                "status": "unused",
                "message": None,
            },
        }

    def test_create_from_json(self):
        webhook_json = self.webhook_json
        webhook = Webhook.objects.create_from_json(repo=self.repo1,
                                                   webhook_json=webhook_json)
        self.assertEqual(2, Webhook.objects.count())
        self.assertEqual(webhook.id, 12345678)
        self.assertEqual(webhook.extra_data, webhook_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        webhook_json = self.webhook_json
        webhook = Webhook.objects.update_or_create_from_json(
            webhook_json=webhook_json, repo=self.repo1)
        self.assertEqual(2, Webhook.objects.count())
        self.assertEqual(webhook.id, webhook_json['id'])
        self.assertEqual(webhook.extra_data, webhook_json)

    def test_update_or_create_from_json_exist(self):
        # test `update_or_create_from_json` with an `id` already present
        webhook_json = self.webhook_json
        webhook_json.update({'id': 1})
        webhook = Webhook.objects.update_or_create_from_json(
            webhook_json=webhook_json, repo=self.repo1)
        self.assertEqual(1, Webhook.objects.count())
        self.assertEqual(webhook.id, webhook_json['id'])
        self.assertEqual(webhook.extra_data, webhook_json)


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class GithubOptionsTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={'access_token': 'token123'},
        )
        self.repo1 = Repository.objects.create(
            id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.repo1.users.add(self.u1)
