from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Github

User = get_user_model()


class GithubModelTest(TestCase):

    def create_github(
        self,
        repo_name='test git',
        branch='master',
        repo_url='http://github.com/dhost-project/dhost',
        auto_deploy=False,
        owner=None
    ):
        return Github.objects.create(
            repo_url=repo_url,
            branch=branch,
            repo_name=repo_name,
            auto_deploy=auto_deploy,
            owner=owner
        )

    def test_str(self):
        """
        Test Github's `__str__` function
        """
        user = User.objects.create(username='john', password='john')
        g = self.create_github(owner=user)
        github_str = str(g)
        self.assertTrue(isinstance(g, Github))
        self.assertEqual(str, type(github_str))
