from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from dhost.notifications.models import Notification

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class NotificationViewSetTestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create(username='bill', password='bill')
        cls.u2 = User.objects.create(username='tom', password='tom')
        cls.notif_unread = Notification.objects.create(user=cls.u1,
                                                       subject='unread_subject',
                                                       content='unread_content')
        cls.notif_read = Notification.objects.create(user=cls.u1,
                                                     subject='read',
                                                     content='content...',
                                                     read=True)
        cls.notif_u2 = Notification.objects.create(user=cls.u2,
                                                   subject='unread',
                                                   content='content...')

    def setUp(self):
        self.client.force_authenticate(user=self.u1)

    def test_list_notifications_unauthorized(self):
        url = reverse('api:notifications-list')
        self.client.force_authenticate(user=None)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_notifications(self):
        url = reverse('api:notifications-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_notification_404(self):
        # exist but return 404 because it's not for the user
        url = reverse('api:notifications-detail', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_notification(self):
        url = reverse('api:notifications-detail', args=(self.notif_unread.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('subject', response.data)
        self.assertIn('time', response.data)

    def test_destroy_notification_404(self):
        url = reverse('api:notifications-detail', args=(self.notif_u2.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_notification(self):
        url = reverse('api:notifications-detail', args=(self.notif_unread.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_notification_404(self):
        url = reverse('api:notifications-read', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_read_notification(self):
        url = reverse('api:notifications-read', args=(self.notif_unread.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['read'])

    def test_unread_notification_404(self):
        url = reverse('api:notifications-unread', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unread_notification(self):
        url = reverse('api:notifications-unread', args=(self.notif_unread.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['read'])
