import os
from unittest import mock

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from dhost.dapps.models import Dapp
from dhost.github.models import Branch, GithubOptions, Repository, Webhook

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class TestDataMixin(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username='john', password='john')
        cls.u2 = User.objects.create(username='tom', password='tom')
        cls.s1 = UserSocialAuth.objects.create(
            user=cls.u1,
            provider='github',
            uid='1234',
            extra_data={
                'access_token': 'token123',
                'login': 'octocat'
            },
        )
        cls.repo1 = Repository.objects.create(
            id=1,
            github_owner='octocat',
            github_repo='Hello-World',
            extra_data={'size': 52},
        )
        cls.repo1.users.add(cls.u1)
        cls.repo1_json = {
            "id": 42424242,
            "name": "Hello-World",
            "owner": {
                "login": "octocat",
            },
            "size": 42,
        }
        cls.dapp1 = Dapp.objects.create(owner=cls.u1, slug='dapp_test')
        cls.branch1 = Branch.objects.create(
            repo=cls.repo1,
            name='master',
            extra_data={'name': 'master'},
        )
        cls.branch1_json = {
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
        cls.webhook1 = Webhook.objects.create(repo=cls.repo1, id=1)
        cls.webhook1_json = {
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
        cls.go1 = GithubOptions.objects.create(
            dapp=cls.dapp1,
            repo=cls.repo1,
            branch=cls.branch1,
        )


class RepositoryTestCase(TestDataMixin, TestCase):

    def test_str(self):
        # test Github's `__str__` function
        github_str = str(self.repo1)
        self.assertEqual(str, type(github_str))

    def test_remove_user(self):
        self.repo1.remove_user(self.u1)
        self.assertFalse(self.repo1.users.filter(id=self.u1.id))

    def test_create_from_json(self):
        repo_json = self.repo1_json
        repo = Repository.objects.create_from_json(repo_json=repo_json,
                                                   user=self.u1)
        self.assertEqual(2, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        self.assertTrue(repo.users.filter(id=self.u1.id).exists())
        self.assertTrue(Repository.objects.get(id=42424242))

    def test_update_or_create_from_json_exist(self):
        # if the repo already exist (same id)
        repo_json = self.repo1_json
        repo_json.update({'id': 1})
        repo = Repository.objects.update_or_create_from_json(
            repo_json=repo_json, user=self.u2)
        self.assertEqual(1, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        # the Github repo exist but the user wasn't in it, we are testing that
        # they are added has well
        self.assertTrue(repo.users.filter(id=self.u2.id).exists())

    def test_update_or_create_from_json_doesnt_exist(self):
        repo_json = self.repo1_json
        repo = Repository.objects.update_or_create_from_json(
            repo_json=repo_json, user=self.u1)
        self.assertEqual(2, Repository.objects.count())
        self.assertEqual(repo.id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)
        self.assertTrue(repo.users.filter(id=self.u1.id).exists())

    @mock.patch(
        'dhost.github.github_api.DjangoGithubAPI.list_repos',
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

    def test_remove_unavailable_list_empty(self):
        Repository.objects.remove_unavailable_list([], self.u1)
        # if the list is empty, meaning that he doesn't have access to any
        # Github repos, then he should not be in any repo's `users`
        self.assertEqual(0, Repository.objects.filter(users=self.u1).count())

    @mock.patch(
        'dhost.github.github_api.DjangoGithubAPI.get_repo',
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
        'dhost.github.github_api.DjangoGithubAPI.get_repo',
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
        # if the Github ID doesn't match the local ID we shouldn't update the
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

    @mock.patch('dhost.github.github_api.DjangoGithubAPI.download_repo')
    def test_download_repo(self, download_repo_mock):
        self.repo1.download(user=self.u1,
                            ref='master',
                            base_path=settings.TEST_DIR)
        download_repo_mock.assert_called_once_with(
            owner=self.repo1.github_owner,
            repo=self.repo1.github_repo,
            ref='master',
            path=os.path.join(settings.TEST_DIR, self.repo1.github_repo),
        )

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


class BranchTestCase(TestDataMixin, TestCase):

    def test_create_from_json(self):
        branch_json = self.branch1_json
        branch = Branch.objects.create_from_json(repo=self.repo1,
                                                 branch_json=branch_json)
        self.assertEqual(2, Branch.objects.count())
        self.assertEqual(branch.name, 'master')
        self.assertEqual(branch.extra_data, branch_json)

    def test_update_or_create_from_json_exist(self):
        branch_json = self.branch1_json
        branch = Branch.objects.update_or_create_from_json(
            repo=self.repo1, branch_json=branch_json)
        self.assertEqual(1, Branch.objects.count())
        self.assertEqual(branch.name, 'master')
        self.assertEqual(branch.extra_data, branch_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        branch_json = self.branch1_json
        branch_json.update({'name': 'dev'})
        branch = Branch.objects.update_or_create_from_json(
            repo=self.repo1, branch_json=branch_json)
        self.assertEqual(2, Branch.objects.count())
        self.assertEqual(branch.name, 'dev')
        self.assertEqual(branch.extra_data, branch_json)

    def test_remove_unavailable_list_present(self):
        branch_list = [{'name': 'master'}]
        Branch.objects.remove_unavailable_list(branch_list, self.repo1)
        self.assertEqual(1, Branch.objects.all().count())

    def test_remove_unavailable_list_not_present(self):
        branch_list = [{'name': 'dev'}]
        Branch.objects.remove_unavailable_list(branch_list, self.repo1)
        self.assertEqual(0, self.repo1.branches.all().count())
        # not only remove the link bu also delete the object
        self.assertEqual(0, Branch.objects.all().count())

    @mock.patch(
        'dhost.github.github_api.DjangoGithubAPI.list_branches',
        mock.MagicMock(return_value=[
            {
                "name": "master",
                "extra": "test",
            },
            {
                "name": "dev",
                "extra": "test_dev",
            },
        ]),
    )
    def test_fetch_repo_branches(self):
        Branch.objects.fetch_repo_branches(self.repo1, self.u1)
        # 2 because 1 already exist, and 3 is added but one has the same name
        # as an already existing repo so it will be updated instead.
        self.assertEqual(2, self.repo1.branches.all().count())
        # test that the branch wich already existed was updated
        self.assertEqual(
            Branch.objects.get(name='master', repo=self.repo1).extra_data, {
                "name": "master",
                "extra": "test"
            })
        # test that the new branch was added
        self.assertEqual(
            Branch.objects.get(name='dev', repo=self.repo1).name, 'dev')


class WebhookTestCase(TestDataMixin, TestCase):

    def test_create_from_json(self):
        webhook_json = self.webhook1_json
        webhook = Webhook.objects.create_from_json(repo=self.repo1,
                                                   webhook_json=webhook_json)
        self.assertEqual(2, Webhook.objects.count())
        self.assertEqual(webhook.id, 12345678)
        self.assertEqual(webhook.extra_data, webhook_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        webhook_json = self.webhook1_json
        webhook = Webhook.objects.update_or_create_from_json(
            webhook_json=webhook_json, repo=self.repo1)
        self.assertEqual(2, Webhook.objects.count())
        self.assertEqual(webhook.id, webhook_json['id'])
        self.assertEqual(webhook.extra_data, webhook_json)

    def test_update_or_create_from_json_exist(self):
        # test `update_or_create_from_json` with an `id` already present
        webhook_json = self.webhook1_json
        webhook_json.update({'id': 1})
        webhook = Webhook.objects.update_or_create_from_json(
            webhook_json=webhook_json, repo=self.repo1)
        self.assertEqual(1, Webhook.objects.count())
        self.assertEqual(webhook.id, webhook_json['id'])
        self.assertEqual(webhook.extra_data, webhook_json)

    @mock.patch(
        'dhost.github.github_api.DjangoGithubAPI.create_hook',
        mock.MagicMock(return_value={
            'id': 2,
            'name': 'test_name',
            'active': True,
        }),
    )
    def test_create_webhook(self):
        webhook = Webhook.objects.create_webhook(repo=self.repo1,
                                                 user=self.u1,
                                                 name='test_name')
        self.assertEqual(webhook.name, 'test_name')


class GithubOptionsTestCase(TestDataMixin, TestCase):

    @mock.patch('dhost.github.models.Repository.download')
    def test_download_repo(self, download_repo_mock):
        self.go1.download_repo()
        download_repo_mock.assert_called_once_with(
            user=self.u1,
            ref='master',
            # TODO change MEDIA_ROOT to something else
            base_path=settings.MEDIA_ROOT,
        )
