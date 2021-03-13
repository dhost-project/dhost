from datetime import date

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode

from ..models import User
from ..views import (
    PasswordChangeDoneView, PasswordChangeView, PasswordResetCompleteView,
    PasswordResetDoneView, PasswordResetView
)
from .client import PasswordResetConfirmClient


@override_settings(ROOT_URLCONF='dhost.users.urls')
class AuthTemplateTests(TestCase):
    request_factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user('jsmith', 'jsmith@example.com', 'pass')
        user = authenticate(username=user.username, password='pass')
        request = cls.request_factory.get('/somepath/')
        request.user = user
        cls.user, cls.request = user, request

    def test_password_reset_view(self):
        response = PasswordResetView.as_view(success_url='dummy/')(self.request)
        self.assertContains(response, 'Password reset')

    def test_password_reset_done_view(self):
        response = PasswordResetDoneView.as_view()(self.request)
        self.assertContains(response, 'Password reset sent')

    def test_password_reset_confirm_view_invalid_token(self):
        # PasswordResetConfirmView invalid token
        client = PasswordResetConfirmClient()
        url = reverse(
            'password_reset_confirm',
            kwargs={
                'uidb64': 'Bad',
                'token': 'Bad-Token'
            }
        )
        response = client.get(url)
        self.assertContains(response, 'Password reset unsuccessful')

    def test_password_reset_confirm_view_valid_token(self):
        # PasswordResetConfirmView valid token
        client = PasswordResetConfirmClient()
        default_token_generator = PasswordResetTokenGenerator()
        token = default_token_generator.make_token(self.user)
        uidb64 = urlsafe_base64_encode(str(self.user.pk).encode())
        url = reverse(
            'password_reset_confirm', kwargs={
                'uidb64': uidb64,
                'token': token
            }
        )
        response = client.get(url)
        self.assertContains(response, 'Enter new password')
        # The username is added to the password reset confirmation form to help
        # browser's password managers.
        self.assertContains(
            response,
            '<input class="hidden" autocomplete="username" value="jsmith">',
        )

    def test_password_reset_complete_view(self):
        response = PasswordResetCompleteView.as_view()(self.request)
        self.assertContains(response, 'Password reset complete')

    def test_password_reset_change_view(self):
        response = PasswordChangeView.as_view(success_url='dummy/'
                                             )(self.request)
        self.assertContains(response, 'Password change')

    def test_password_change_done_view(self):
        response = PasswordChangeDoneView.as_view()(self.request)
        self.assertContains(response, 'Password change successful')
