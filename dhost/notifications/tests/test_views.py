from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import override_settings
from django.urls import reverse
from rest_framework import routers, status
from rest_framework.test import APITestCase, URLPatternsTestCase

from dhost.notifications.models import Notification
from dhost.notifications.views import NotificationViewSet

User = get_user_model()


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class NotificationViewSetTestCase(APITestCase, URLPatternsTestCase):

    router = routers.SimpleRouter()
    router.register('tests', NotificationViewSet, basename='notifications')
    urlpatterns = router.urls

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
        url = reverse('notifications-list')
        self.client.force_authenticate(user=None)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_notifications(self):
        url = reverse('notifications-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_notification_404(self):
        # exist but return 404 because it's not for the user
        url = reverse('notifications-detail', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_notification(self):
        url = reverse('notifications-detail', args=(self.notif_unread.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['subject'], self.notif_unread.subject)
        self.assertIn('timestamp', response.data)

    def test_destroy_notification_404(self):
        url = reverse('notifications-detail', args=(self.notif_u2.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_destroy_notification(self):
        url = reverse('notifications-detail', args=(self.notif_unread.id,))
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_read_notification_404(self):
        url = reverse('notifications-read', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_read_notification(self):
        url = reverse('notifications-read', args=(self.notif_unread.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['read'])
        self.assertTrue(Notification.objects.get(id=self.notif_unread.id).read)

    def test_unread_notification_404(self):
        url = reverse('notifications-unread', args=(self.notif_u2.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unread_notification(self):
        url = reverse('notifications-unread', args=(self.notif_read.id,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(response.data['read'])
        self.assertFalse(Notification.objects.get(id=self.notif_read.id).read)

    def test_mark_all_as_read_notification(self):
        url = reverse('notifications-mark-all-as-read')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertTrue(Notification.objects.get(id=self.notif_unread.id).read)

    def test_mark_all_as_read_notification_none_to_read(self):
        url = reverse('notifications-mark-all-as-read')
        self.notif_unread.read = True
        self.notif_unread.save()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_mark_all_as_unread_notification(self):
        url = reverse('notifications-mark-all-as-unread')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertFalse(Notification.objects.get(id=self.notif_read.id).read)

    def test_mark_all_as_unread_notification_none_to_unread(self):
        url = reverse('notifications-mark-all-as-unread')
        self.notif_read.read = False
        self.notif_read.save()
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 0)

    def test_unread_count(self):
        url = reverse('notifications-unread-count')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['count'], 1)

    def test_count(self):
        url = reverse('notifications-count')
        response = self.client.get(url, format='json')
        self.assertEqual(response.data['count'], 2)
