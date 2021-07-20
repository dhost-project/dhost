from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, override_settings

from dhost.dapps.models import Dapp
from dhost.logs.models import ActionFlags, APILog

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class APILogTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username="john", password="john")
        cls.dapp1 = Dapp.objects.create(slug="test", owner=cls.u1)

    def test_log_create(self):
        log = APILog.objects.create(
            user=self.u1,
            dapp=self.dapp1,
            content_type=ContentType.objects.get_for_model(self.dapp1),
            object_id=self.dapp1.pk,
            action_flag=ActionFlags.DAPP_ADDITION,
            change_message="test",
        )
        self.assertTrue(isinstance(log, APILog))
        self.assertEqual(str, type(log.__str__()))
        self.assertIn("test", str(log))
