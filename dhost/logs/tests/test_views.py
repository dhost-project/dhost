from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import include, path, reverse
from rest_framework import routers, status
from rest_framework.test import APITestCase, URLPatternsTestCase

from dhost.dapps.models import Dapp
from dhost.logs.models import APILog
from dhost.logs.views import APILogViewSet

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class APILogViewSetTestCase(APITestCase, URLPatternsTestCase):

    router = routers.SimpleRouter()
    router.register('tests', APILogViewSet, basename='dapp_log')
    urlpatterns = [path('<slug:dapp_slug>/', include(router.urls))]

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username='bill', password='bill')
        cls.u2 = User.objects.create(username='tom', password='tom')
        cls.dapp1 = Dapp.objects.create(slug='dapp1', owner=cls.u1)
        cls.dapp2 = Dapp.objects.create(slug='dapp2', owner=cls.u2)
        cls.log1 = APILog.objects.create(user=cls.u1, dapp=cls.dapp1)
        cls.log2 = APILog.objects.create(user=cls.u1, dapp=cls.dapp2)
        cls.log3 = APILog.objects.create(user=cls.u2, dapp=cls.dapp1)

    def setUp(self):
        self.client.force_authenticate(user=self.u1)

    def test_list_log_unauthorized(self):
        # if the user is not logged in
        url = reverse('dapp_log-list', args=(self.dapp1.slug,))
        self.client.force_authenticate(user=None)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_log_404_not_dapp_owner(self):
        # if the user is not the dapp owner
        url = reverse('dapp_log-list', args=(self.dapp2.slug,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_log(self):
        # if the user is the dapp owner
        url = reverse('dapp_log-list', args=(self.dapp1.slug,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_log_404_missmatch_dapp_and_log(self):
        # both log and dapp exist but the log is not from this dapp
        url = reverse('dapp_log-detail', args=(self.dapp2.slug, self.log1.id))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_log_404_not_owner_of_dapp(self):
        # exist but return 404 because it's not for the user
        url = reverse('dapp_log-detail', args=(self.dapp2.slug, self.log2.id))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_log(self):
        url = reverse('dapp_log-detail', args=(self.dapp1.slug, self.log1.id))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('action_flag', response.data)
        self.assertIn('action_time', response.data)
