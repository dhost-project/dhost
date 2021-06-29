from django.db import models
from oauth2_provider.models import AbstractApplication

from dhost.utils.avatar import avatar_generator


class Application(AbstractApplication):
    logo = models.ImageField(
        upload_to='oauth2_provider_app_logos/',
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)

    class Meta(AbstractApplication.Meta):
        pass

    def save(self, *args, **kwargs):
        if not self.logo:
            # if the logo doesn't exist it will be generated from a hash of
            # the client_id field
            # to 're-generate' the logo simply remove it and save the app or
            # call the function `generate_logo` and don't forget to `save`
            self.generate_logo()
        return super().save(*args, **kwargs)

    def generate_logo(self):
        # client_id is unique
        self.logo = avatar_generator(self.client_id)
