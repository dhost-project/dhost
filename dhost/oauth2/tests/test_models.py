from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from dhost.oauth2.models import Application

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class ApplicationTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user("test_user", "test@example.com",
                                            "123456")
        cls.application = Application.objects.create(
            name="Test Application",
            redirect_uris="",
            user=cls.user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        )

    def test_autogenerate_logo(self):
        self.assertTrue(self.application.logo)
