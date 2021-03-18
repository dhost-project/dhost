import shutil

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Delete test dir folder.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput',
            '--no-input',
            action='store_false',
            dest='interactive',
            help='Tells Django to NOT prompt the user for input of any kind.',
        )

    def handle(self, *args, **options):
        interactive = options['interactive']

        if interactive:
            confirm = input("""You have requested to remove the test folder.
This will IRREVERSIBLY DESTROY all data currently in the "%s" folder.
Are you sure you want to do this?

    Type 'yes' to continue, or 'no' to cancel: """ % settings.TEST_DIR)
        else:
            confirm = 'yes'

        if confirm == 'yes':
            try:
                shutil.rmtree(settings.TEST_DIR)
                return 'Test dir successfully deleted'
            except OSError:
                raise CommandError('Error while deleting test dir.')
        else:
            self.stdout.write('Flush cancelled.')
