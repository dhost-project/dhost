"""Django's command-line utility for administrative tasks."""
import os
import sys

from dhost.utils import generate_version

# used to generate the version, get git hash with: git rev-parse --short HEAD
__git_hash__ = '0ecf1c6'

# https://www.python.org/dev/peps/pep-0440/
__version__ = generate_version('1.2.dev{}', git_hash=__git_hash__)

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'development')


def prepare_env():

    if DJANGO_ENV not in ['development', 'production']:
        raise Exception(
            "The `DJANGO_ENV` environment variable can only be one of two: "
            "`development` or `production`.")

    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'dhost.settings.{DJANGO_ENV}'.format(DJANGO_ENV=DJANGO_ENV))


def manage():
    """Run administrative tasks."""
    prepare_env()

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?") from exc

    execute_from_command_line(sys.argv)
