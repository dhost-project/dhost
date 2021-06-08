from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from ..models import GithubRepo

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class GithubRepoTestCase(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data={'access_token': 'token123'},
        )
        self.repo1 = GithubRepo.objects.create(
            owner=self.s1,
            name='dhost-front',
            github_id=1,
            github_owner='dhost-project',
            github_repo='dhost-front',
            github_extra_data={'size': 52},
        )

    def test_str(self):
        """
        Test Github's `__str__` function
        """
        github_str = str(self.repo1)
        self.assertEqual(str, type(github_str))

    def test_create_from_json(self):
        repo_json = {
            "id": 191538244,
            "name": "MineSweeper",
            "owner": {
                "login": "2O4",
            },
            "size": 42,
        }
        nbr_repos = GithubRepo.objects.count()
        repo = GithubRepo.objects.create_from_json(owner=self.s1,
                                                   repo_json=repo_json)
        nbr_repos_after = GithubRepo.objects.count()
        self.assertEqual(nbr_repos + 1, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.github_extra_data, repo_json)

    def test_update_or_create_from_json_exist(self):
        repo_json = {
            "id": 1,
            "name": "dhost-front",
            "owner": {
                "login": "dhost-project",
            },
            "size": 42,
        }
        nbr_repos = GithubRepo.objects.count()
        repo = GithubRepo.objects.update_or_create_from_json(
            owner=self.s1, repo_json=repo_json)
        nbr_repos_after = GithubRepo.objects.count()
        self.assertEqual(nbr_repos, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.github_extra_data, repo_json)

    def test_update_or_create_from_json_doesnt_exist(self):
        repo_json = {
            "id": 191538244,
            "name": "MineSweeper",
            "owner": {
                "login": "2O4",
            },
            "size": 42,
        }
        nbr_repos = GithubRepo.objects.count()
        repo = GithubRepo.objects.update_or_create_from_json(
            owner=self.s1, repo_json=repo_json)
        nbr_repos_after = GithubRepo.objects.count()
        self.assertEqual(nbr_repos + 1, nbr_repos_after)
        self.assertEqual(repo.github_id, repo_json['id'])
        self.assertEqual(repo.github_extra_data, repo_json)

    # mock 'get_repos' function
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
