from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from dhost.github.github import DjangoGithubAPI

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class DjangoGithubAPITestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.u = User.objects.create(username='john', password='john')
        cls.s = UserSocialAuth.objects.create(
            user=cls.u,
            provider='github',
            uid='1234',
            extra_data={
                'access_token': 'token123',
                'login': 'john'
            },
        )
        cls.dg = DjangoGithubAPI(user=cls.u)

    def test_get_token(self):
        # test that the token come from the user's social account
        self.assertEqual(self.dg.get_token(), 'token123')
