from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings
from social_django.models import UserSocialAuth

from dhost.github.utils import (
    get_token_from_github_account,
    get_user_github_account,
    user_has_github_account,
)

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class UtilsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username="john", password="john")
        cls.u2 = User.objects.create(username="tom", password="tom")
        cls.u3 = User.objects.create(username="tim", password="tim")
        cls.s1 = UserSocialAuth.objects.create(
            user=cls.u1,
            provider="github",
            uid="1234",
            extra_data={"access_token": "token123", "login": "john"},
        )
        cls.s2 = UserSocialAuth.objects.create(
            user=cls.u3,
            provider="github",
            uid="2345",
            extra_data={"login": "john"},
        )

    def test_user_has_github_account_true(self):
        self.assertTrue(user_has_github_account(self.u1))

    def test_user_has_github_account_false(self):
        self.assertFalse(user_has_github_account(self.u2))

    def test_get_user_github_account_exist(self):
        self.assertEqual(get_user_github_account(self.u1), self.s1)

    def test_get_user_github_account_doesnt_exist(self):
        with self.assertRaises(Exception) as context:
            get_user_github_account(self.u2)
        self.assertIn("Github account not linked.", str(context.exception))

    def test_get_token_from_github_account_present(self):
        token = get_token_from_github_account(self.s1)
        self.assertEqual(token, "token123")

    def test_get_token_from_github_account_not_present(self):
        with self.assertRaises(Exception) as context:
            get_token_from_github_account(self.s2)
        self.assertIn("'access_token' missing", str(context.exception))
