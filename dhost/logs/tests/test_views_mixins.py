from django.conf import settings
from django.test import TestCase, override_settings

from dhost.logs.views_mixins import APILogViewSetMixin


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class APILogViewSetMixinTestCase(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username='john', password='john')
        self.dapp1 = Dapp.objects.create(slug='test', owner=self.u1)
