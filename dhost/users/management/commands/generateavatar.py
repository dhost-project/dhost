from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS

UserModel = get_user_model()


class Command(BaseCommand):
    help = 'Generate an avatar for a user'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument(
            'username',
            nargs='?',
            help='Username to generate the avatar for.',
        )
        parser.add_argument(
            '--database',
            default=DEFAULT_DB_ALIAS,
            help='Specifies the database to use. Default is "default".',
        )

    def handle(self, *args, **options):
        if options['username']:
            username = options['username']
        else:
            username = input('username: ')

        try:
            u = UserModel._default_manager.using(
                options['database']).get(**{UserModel.USERNAME_FIELD: username})
        except UserModel.DoesNotExist:
            raise CommandError("user '%s' does not exist" % username)

        u.generate_avatar()
        u.save()

        return "Avatar successfully generated for user '%s'" % u
