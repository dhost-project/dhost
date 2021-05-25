import os
import shutil
from io import StringIO
from unittest import mock

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class DelTestDirTest(TestCase):

    def setUp(self):
        # Creating TEST_DIR folder if it doesn't exist
        if not os.path.isdir(settings.TEST_DIR):
            os.mkdir(settings.TEST_DIR)

    def test_command_output(self):
        out = StringIO()
        call_command('deltestdir', '--noinput', stdout=out)
        self.assertIn(settings.TEST_DIR, out.getvalue())
        self.assertFalse(os.path.isdir(settings.TEST_DIR))

    def test_folder_doesnt_exist(self):
        shutil.rmtree(settings.TEST_DIR)
        out = StringIO()
        call_command('deltestdir', '--noinput', stdout=out)
        self.assertIn('Test dir does not exist', out.getvalue())

    @mock.patch('builtins.input', lambda *args: 'yes')
    def test_interactive_yes(self):
        out = StringIO()
        call_command('deltestdir', stdout=out)
        self.assertFalse(os.path.isdir(settings.TEST_DIR))

    @mock.patch('builtins.input', lambda *args: 'no')
    def test_interactive_no(self):
        out = StringIO()
        call_command('deltestdir', stdout=out)
        self.assertTrue(os.path.isdir(settings.TEST_DIR))
        self.assertIn('cancelled', out.getvalue())
