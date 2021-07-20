from django.core.management import call_command
from django.core.management.commands.test import Command as TestCommand


class Command(TestCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--keepdata",
            "--keep-data",
            action="store_true",
            help="Tells Django to NOT delete the test dir.",
        )

        super().add_arguments(parser)

    def handle(self, *test_labels, **options):
        super().handle(*test_labels, **options)

        if not options.get("keepdata", False):
            call_command("deltestdir", "--noinput")
