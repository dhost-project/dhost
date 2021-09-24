import os
import shutil

from django.core.management.base import BaseCommand

from dhost.utils import get_version


class Command(BaseCommand):
    help = "Show DHost version."

    def handle(self, *args, **options):
        return f"DHost version {get_version()}"
