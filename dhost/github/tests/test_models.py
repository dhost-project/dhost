from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from ..models import Branch, Repository, Webhook

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class RepositoryTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={'access_token': 'token123'},
        )
        self.repo1 = Repository.objects.create(
            owner=self.u1,
            github_id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
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

    def test_create_from_json(self):
        repo_json = self.repo_json
        nbr_repos = Repository.objects.count()
        repo = Repository.objects.create_from_json(owner=self.u1,
                                                   repo_json=repo_json)
        nbr_repos_after = Repository.objects.count()
        self.assertEqual(nbr_repos + 1, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)

    def test_update_or_create_from_json_exist(self):
        repo_json = self.repo_json
        repo_json.update({'id': 1})
        nbr_repos = Repository.objects.count()
        repo = Repository.objects.update_or_create_from_json(
            owner=self.u1, repo_json=repo_json)
        nbr_repos_after = Repository.objects.count()
        self.assertEqual(nbr_repos, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        repo_json = self.repo_json
        nbr_repos = Repository.objects.count()
        repo = Repository.objects.update_or_create_from_json(
            owner=self.u1, repo_json=repo_json)
        nbr_repos_after = Repository.objects.count()
        self.assertEqual(nbr_repos + 1, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.extra_data, repo_json)

    # mock 'list_repos' function
    def test_fetch_all(self):
        pass

    # mock 'get_repo' function
    def test_fetch_repo(self):
        pass

    def test_update_from_json(self):
        pass

    # mock 'downlaod_repo' function
    def test_download_repo(self):
        pass


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
            owner=self.u1,
            github_id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.branch1 = Branch.objects.create(
            repo=self.repo1,
            name='master',
            extra_data={'name': 'master'},
        )
        self.branch_json = {
            "name": "master",
            "commit": {
                "sha": "c5b97d5ae6c19d5c5df71a34c7fbeeda2479ccbc",
                "url": ""
            },
            "protected": True,
            "protection": {
                "required_status_checks": {
                    "enforcement_level": "non_admins",
                    "contexts": ["ci-test", "linter"]
                }
            },
            "protection_url": ""
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
            owner=self.u1,
            github_id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            extra_data={'size': 52},
        )
        self.webhook1 = Webhook.objects.create(
            repo=self.repo1,
            github_id=1,
        )
        self.webhook_json = {
            "type": "Repository",
            "id": 12345678,
            "name": "web",
            "active": True,
            "events": ["push", "pull_request"],
            "config": {
                "content_type": "json",
                "insecure_ssl": "0",
                "url": "https://example.com/webhook"
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
            }
        }

    def test_create_from_json(self):
        webhook_json = self.webhook_json
        webhook = Webhook.objects.create_from_json(repo=self.repo1,
                                                   webhook_json=webhook_json)
        self.assertEqual(2, Webhook.objects.count())
        self.assertEqual(webhook.github_id, 12345678)
        self.assertEqual(webhook.extra_data, webhook_json)
