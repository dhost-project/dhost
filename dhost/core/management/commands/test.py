import os
import shutil

from django.conf import settings
from django.core.management.base import CommandError
from django.core.management.commands.test import Command as TestCommand


class Command(TestCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--keepdata',
            action='store_true',
            help='Tells Django to NOT delete the test dir.',
        )

        super().add_arguments(parser)

    def handle(self, *test_labels, **options):
        super().handle(*test_labels, **options)

        if not options.get('keepdata', False):
            try:
                if os.path.isdir(settings.TEST_DIR):
                    shutil.rmtree(settings.TEST_DIR)
                    return "Removing test dir at '{}'...".format(
                        settings.TEST_DIR)
                else:
                    return "Test dir did not exist at '{}'".format(
                        settings.TEST_DIR)
            except OSError:
                raise CommandError('Error while deleting test dir.')
