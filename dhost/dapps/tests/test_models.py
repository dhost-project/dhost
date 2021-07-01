from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings, tag

from dhost.dapps.models import Dapp

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class DappModelTest(TestCase):

    def create_dapp(
        self,
        slug='test_dapp',
        url='http://example.com/',
        owner=None,
    ):
        return Dapp.objects.create(slug=slug, url=url, owner=owner)

    @tag('fast')
    def test_str(self):
        # test Dapp's `__str__` function
        user = User.objects.create(
            username='johnny',
            password='john',
            avatar='-',
        )
        d = self.create_dapp(owner=user)
        dapp_str = str(d)
        self.assertTrue(isinstance(d, Dapp))
        self.assertEqual(str, type(dapp_str))
