import os
from io import StringIO

from django.conf import settings
from django.core.management import CommandError, call_command
from django.test import TestCase, override_settings, tag

from dhost.users.models import User


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class DelTestDirTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='avataruser',
            password='password',
            email='testclient@example.com',
        )
        self.avatar_path = os.path.join(settings.TEST_MEDIA_ROOT, 'avatars',
                                        'avataruser.png')

        # Avatar is automatically generated when a user is created, we are
        # testing if it's created with this command so we delete it
        if os.path.exists(self.avatar_path):
            os.remove(self.avatar_path)

    @tag('slow')
    def test_command_output(self):
        out = StringIO()
        call_command('generateavatar', 'avataruser', stdout=out)
        self.assertIn('Avatar successfully generated', out.getvalue())
        self.assertTrue(os.path.isfile(self.avatar_path))

    @tag('fast')
    def test_user_does_not_exist_error_message(self):
        """Calling generateavatar produces an error when username is not a
        valid user
        """
        with self.assertRaisesMessage(CommandError,
                                      "User 'nonexistinguser' does not exist."):
            call_command('generateavatar', 'nonexistinguser')
