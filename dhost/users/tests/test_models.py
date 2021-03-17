from unittest import mock

from django.conf import settings
from django.conf.global_settings import PASSWORD_HASHERS
from django.contrib.auth import authenticate, get_user, get_user_model
from django.contrib.auth.hashers import get_hasher
from django.contrib.auth.models import AnonymousUser
from django.core import mail
from django.db import IntegrityError
from django.http import HttpRequest
from django.test import TestCase, override_settings, tag
from django.utils import translation

from dhost.users.models import User


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class UserTestCase(TestCase):

    @tag('core', 'slow')
    def test_user(self):
        "Users can be created and can set their password"
        u = User.objects.create_user('testuser', 'test@example.com', 'testpw')
        self.assertTrue(u.has_usable_password())
        self.assertFalse(u.check_password('bad'))
        self.assertTrue(u.check_password('testpw'))

        # Check we can manually set an unusable password
        u.set_unusable_password()
        u.save()
        self.assertFalse(u.check_password('testpw'))
        self.assertFalse(u.has_usable_password())
        u.set_password('testpw')
        self.assertTrue(u.check_password('testpw'))
        u.set_password(None)
        self.assertFalse(u.has_usable_password())

        # Check username getter
        self.assertEqual(u.get_username(), 'testuser')

        # Check authentication/permissions
        self.assertFalse(u.is_anonymous)
        self.assertTrue(u.is_authenticated)
        self.assertFalse(u.is_staff)
        self.assertTrue(u.is_active)
        self.assertFalse(u.is_superuser)

        # Check API-based user creation with no password
        u2 = User.objects.create_user('testuser2', 'test2@example.com')
        self.assertFalse(u2.has_usable_password())

    @tag('fast')
    def test_unicode_username(self):
        User.objects.create_user('jörg')
        User.objects.create_user('Григорий')
        # Two equivalent Unicode normalized usernames are duplicates.
        omega_username = 'iamtheΩ'  # U+03A9 GREEK CAPITAL LETTER OMEGA
        ohm_username = 'iamtheΩ'  # U+2126 OHM SIGN
        User.objects.create_user(ohm_username)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(omega_username)

    @tag('fast')
    def test_user_no_email(self):
        "Users can be created without an email"
        cases = [
            {},
            {
                'email': ''
            },
            {
                'email': None
            },
        ]
        for i, kwargs in enumerate(cases):
            with self.subTest(**kwargs):
                u = User.objects.create_user('testuser{}'.format(i), **kwargs)
                self.assertEqual(u.email, '')

    def test_superuser(self):
        "Check the creation and properties of a superuser"
        super = User.objects.create_superuser(
            'super', 'super@example.com', 'super'
        )
        self.assertTrue(super.is_superuser)
        self.assertTrue(super.is_active)
        self.assertTrue(super.is_staff)

    def test_superuser_no_email_or_password(self):
        cases = [
            {},
            {
                'email': ''
            },
            {
                'email': None
            },
            {
                'password': None
            },
        ]
        for i, kwargs in enumerate(cases):
            with self.subTest(**kwargs):
                superuser = User.objects.create_superuser(
                    'super{}'.format(i), **kwargs
                )
                self.assertEqual(superuser.email, '')
                self.assertFalse(superuser.has_usable_password())

    def test_get_user_model(self):
        "The current user model can be retrieved"
        self.assertEqual(get_user_model(), User)

    @tag('translation')
    def test_user_verbose_names_translatable(self):
        "Default User model verbose names are translatable"
        with translation.override('en'):
            self.assertEqual(User._meta.verbose_name, 'user')
            self.assertEqual(User._meta.verbose_name_plural, 'users')
        with translation.override('es'):
            self.assertEqual(User._meta.verbose_name, 'usuario')
            self.assertEqual(User._meta.verbose_name_plural, 'usuarios')

    @tag('core', 'slow')
    def test_authenticate(self):
        test_user = User.objects.create_user(
            username='username',
            email='test@example.com',
            password='test',
        )
        authenticated_user = authenticate(username='username', password='test')
        self.assertEqual(test_user, authenticated_user)

    @tag('core')
    def test_email_user(self):
        # valid send_mail parameters
        kwargs = {
            "fail_silently": False,
            "auth_user": None,
            "auth_password": None,
            "connection": None,
            "html_message": None,
        }
        user = User(email='foo@bar.com')
        user.email_user(
            subject="Subject here",
            message="This is a message",
            from_email="from@domain.com",
            **kwargs
        )
        self.assertEqual(len(mail.outbox), 1)
        message = mail.outbox[0]
        self.assertEqual(message.subject, "Subject here")
        self.assertEqual(message.body, "This is a message")
        self.assertEqual(message.from_email, "from@domain.com")
        self.assertEqual(message.to, [user.email])

    @tag('fast')
    def test_last_login_default(self):
        user1 = User.objects.create(username='user1')
        self.assertIsNone(user1.last_login)

        user2 = User.objects.create_user(username='user2')
        self.assertIsNone(user2.last_login)

    @tag('fast')
    def test_user_clean_normalize_email(self):
        user = User(username='user', password='foo', email='foo@BAR.com')
        user.clean()
        self.assertEqual(user.email, 'foo@bar.com')

    @tag('fast')
    def test_user_double_save(self):
        """
        Calling user.save() twice should trigger password_changed() once.
        """
        user = User.objects.create_user(username='user', password='foo')
        user.set_password('bar')
        with mock.patch(
            'django.contrib.auth.password_validation.password_changed'
        ) as pw_changed:
            user.save()
            self.assertEqual(pw_changed.call_count, 1)
            user.save()
            self.assertEqual(pw_changed.call_count, 1)

    @tag('core')
    @override_settings(PASSWORD_HASHERS=PASSWORD_HASHERS)
    def test_check_password_upgrade(self):
        """
        password_changed() shouldn't be called if User.check_password()
        triggers a hash iteration upgrade.
        """
        user = User.objects.create_user(username='user', password='foo')
        initial_password = user.password
        self.assertTrue(user.check_password('foo'))
        hasher = get_hasher('default')
        self.assertEqual('pbkdf2_sha256', hasher.algorithm)

        old_iterations = hasher.iterations
        try:
            # Upgrade the password iterations
            hasher.iterations = old_iterations + 1
            with mock.patch(
                'django.contrib.auth.password_validation.password_changed'
            ) as pw_changed:
                user.check_password('foo')
                self.assertEqual(pw_changed.call_count, 0)
            self.assertNotEqual(initial_password, user.password)
        finally:
            hasher.iterations = old_iterations

    def test_get_user_anonymous(self):
        request = HttpRequest()
        request.session = self.client.session
        user = get_user(request)
        self.assertIsInstance(user, AnonymousUser)

    def test_get_user(self):
        created_user = User.objects.create_user(
            'testuser', 'test@example.com', 'testpw'
        )
        self.client.login(username='testuser', password='testpw')
        request = HttpRequest()
        request.session = self.client.session
        user = get_user(request)
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, created_user.username)
