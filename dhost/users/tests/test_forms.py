from django.conf import settings
from django.forms.fields import Field
from django.test import TestCase, override_settings, tag

from ..forms import AccountSettingsForm, SignupForm
from ..models import User


class TestDataMixin:

    @classmethod
    def setUpTestData(cls):
        cls.u1 = User.objects.create_user(
            username='testclient',
            password='password',
            email='testclient@example.com'
        )
        cls.u2 = User.objects.create_user(
            username='inactive', password='password', is_active=False
        )
        cls.u3 = User.objects.create_user(username='staff', password='password')
        cls.u4 = User.objects.create(username='empty_password', password='')
        cls.u5 = User.objects.create(
            username='unmanageable_password', password='$'
        )
        cls.u6 = User.objects.create(
            username='unknown_password', password='foo$bar'
        )


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class SignupFormTest(TestDataMixin, TestCase):

    def test_user_already_exists(self):
        data = {
            'username': 'testclient',
            'password1': 'test123!',
            'password2': 'test123!',
        }
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form["username"].errors,
            [str(User._meta.get_field('username').error_messages['unique'])]
        )

    def test_invalid_data(self):
        data = {
            'username': 'jsmith!',
            'password1': 'test123!',
            'password2': 'test123!',
        }
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        validator = next(
            v for v in User._meta.get_field('username').validators
            if v.code == 'invalid'
        )
        self.assertEqual(form["username"].errors, [str(validator.message)])

    def test_password_verification(self):
        # The verification password is incorrect.
        data = {
            'username': 'jsmith',
            'password1': 'test123!',
            'password2': 'test',
        }
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form["password2"].errors,
            [str(form.error_messages['password_mismatch'])]
        )

    @tag('core')
    def test_both_passwords(self):
        # One (or both) passwords weren't given
        data = {'username': 'jsmith'}
        form = SignupForm(data)
        required_error = [str(Field.default_error_messages['required'])]
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, required_error)
        self.assertEqual(form['password2'].errors, required_error)

        data['password2'] = 'test123*'
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, required_error)
        self.assertEqual(form['password2'].errors, [])

    def test_unicode_username(self):
        data = {
            'username': '宝',
            'password1': 'test123!',
            'password2': 'test123!',
        }
        form = SignupForm(data)
        self.assertTrue(form.is_valid())
        u = form.save()
        self.assertEqual(u.username, '宝')

    def test_normalize_username(self):
        # The normalization happens in AbstractBaseUser.clean() and ModelForm
        # validation calls Model.clean().
        ohm_username = 'testΩ'  # U+2126 OHM SIGN
        data = {
            'username': ohm_username,
            'password1': 'test123!',
            'password2': 'test123!',
        }
        form = SignupForm(data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertNotEqual(user.username, ohm_username)
        self.assertEqual(
            user.username, 'testΩ'
        )  # U+03A9 GREEK CAPITAL LETTER OMEGA

    def test_duplicate_normalized_unicode(self):
        """
        To prevent almost identical usernames, visually identical but differing
        by their unicode code points only, Unicode NFKC normalization should
        make appear them equal to Django.
        """
        omega_username = 'iamtheΩ'  # U+03A9 GREEK CAPITAL LETTER OMEGA
        ohm_username = 'iamtheΩ'  # U+2126 OHM SIGN
        self.assertNotEqual(omega_username, ohm_username)
        User.objects.create_user(username=omega_username, password='pwd')
        data = {
            'username': ohm_username,
            'password1': 'test123!',
            'password2': 'test123!',
        }
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            ["A user with that username already exists."]
        )

    def test_validates_password(self):
        data = {
            'username': 'ok45u',
            'password1': 'ok45u!',
            'password2': 'ok45u!',
        }
        form = SignupForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form['password2'].errors), 2)
        self.assertIn(
            'The password is too similar to the username.',
            form['password2'].errors
        )
        self.assertIn(
            'This password is too short. It must contain at least 8 '
            'characters.', form['password2'].errors
        )

    def test_password_whitespace_not_stripped(self):
        data = {
            'username': 'testuser',
            'password1': '   testpassword   ',
            'password2': '   testpassword   ',
        }
        form = SignupForm(data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['password1'], data['password1'])
        self.assertEqual(form.cleaned_data['password2'], data['password2'])

    def test_username_field_autocapitalize_none(self):
        form = SignupForm()
        self.assertEqual(
            form.fields['username'].widget.attrs.get('autocapitalize'), 'none'
        )

    def test_html_autocomplete_attributes(self):
        form = SignupForm()
        tests = (
            ('username', 'username'),
            ('password1', 'new-password'),
            ('password2', 'new-password'),
        )
        for field_name, autocomplete in tests:
            with self.subTest(field_name=field_name, autocomplete=autocomplete):
                self.assertEqual(
                    form.fields[field_name].widget.attrs['autocomplete'],
                    autocomplete
                )


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class AccountSettingsFormTest(TestDataMixin, TestCase):

    def test_valide_data(self):
        data = {
            'username': 'john',
        }
        form = AccountSettingsForm(data, instance=self.u1)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['username'], data['username'])

    def test_username_field_autocapitalize_none(self):
        form = AccountSettingsForm()
        self.assertEqual(
            form.fields['username'].widget.attrs.get('autocapitalize'), 'none'
        )
