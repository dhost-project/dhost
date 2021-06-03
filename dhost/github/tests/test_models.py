from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from ..models import GithubRepo

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class GithubModelTest(TestCase):

    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.s1 = UserSocialAuth.objects.create(
            user=self.u1,
            provider='github',
            uid='1234',
            extra_data = {'access_token': 'token123'},
        )
        self.repo1 = GithubRepo.objects.create(
            owner=self.s1,
            name='dhost-front',
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

    def test_create_from_api(self):
        pass
