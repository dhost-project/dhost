from django.db import models
from oauth2_provider.models import AbstractApplication


class Application(AbstractApplication):
    logo = models.ImageField(
        upload_to='oauth2_provider_app_logos/',
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)

    class Meta(AbstractApplication.Meta):
        pass
