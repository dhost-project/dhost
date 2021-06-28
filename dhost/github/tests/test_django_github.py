from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from dhost.github.github import DjangoGithubAPI

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class DjangoGithubAPITestCase(TestCase):

    def setUp(self):
        self.u = User.objects.create(username='john', password='john')
        self.s = UserSocialAuth.objects.create(
            user=self.u,
            provider='github',
            uid='1234',
            extra_data={
                'access_token': 'token123',
                'login': 'john'
            },
        )
        self.dg = DjangoGithubAPI(user=self.u)

    def test_get_token(self):
        # Test that the token come from the user's social account
        self.assertEqual(self.dg.get_token(), 'token123')
