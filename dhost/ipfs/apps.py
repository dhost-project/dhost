from django.apps import AppConfig


class IPFSConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "dhost.ipfs"
    def ready(self):
        import dhost.ipfs.signals  # noqa5.
