from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Dapp

User = get_user_model()


class DappModelTest(TestCase):

    def create_dapp(
        self,
        name='test dapp',
        url='http://example.com/',
        owner=None,
    ):
        return Dapp.objects.create(name=name, url=url, owner=owner)

    def test_str(self):
        """
        Test Dapp's `__str__` function
        """
        user = User.objects.create(
            username='johnny',
            password='john',
            avatar='-',
        )
        d = self.create_dapp(owner=user)
        dapp_str = str(d)
        self.assertTrue(isinstance(d, Dapp))
        self.assertEqual(str, type(dapp_str))
