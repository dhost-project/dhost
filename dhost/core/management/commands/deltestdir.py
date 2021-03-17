import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete test dir folder.'

    def handle(self, *args, **options):

        try:
            shutil.rmtree(settings.TEST_DIR)
        except OSError:
            raise CommandError('Error while deleting test dir.')

        return "Test dir successfully deleted"
