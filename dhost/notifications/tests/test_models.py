from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings

from dhost.notifications.models import Notification

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class APILogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username="john", password="john")
        cls.notif_unread = Notification.objects.create(
            user=cls.u1, subject="unread", content="content..."
        )
        cls.notif_read = Notification.objects.create(
            user=cls.u1, subject="read", content="content...", read=True
        )

    def test__str__(self):
        self.assertEqual(str, type(self.notif_unread.__str__()))

    def test_default_unread(self):
        self.assertFalse(self.notif_unread.read)

    def test_read_by_user(self):
        self.notif_unread.mark_as_read()
        self.assertTrue(self.notif_unread.read)

    def test_unread_by_user(self):
        self.notif_read.mark_as_unread()
        self.assertFalse(self.notif_read.read)
