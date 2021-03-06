from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Dapp(models.Model):
    name = models.CharField(
        _('dapp name'),
        max_length=128,
        unique=True,
        error_messages={
            'unique': _("A dapp with that name already exists."),
        },
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="dapps",
        related_query_name="dapps",
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=2048, blank=True)
    source = models.FilePathField(null=True, blank=True)
    bundle = models.FilePathField(null=True, blank=True)
    docker_container = models.CharField(max_length=128, blank=True)

    class Statuses(models.TextChoices):
        STOPED = 'SO', _('Stoped')
        BUILDING = 'BI', _('Building')
        BUILT = 'BT', _('Builed')
        DEPLOYING = 'DP', _('Deploying')
        STARTING = 'SA', _('Starting')
        UP = 'UP', _('Running')
        UNAVAILABLE = 'UA', _('Unavailable')

    status = models.CharField(max_length=2, choices=Statuses.choices, default=Statuses.STOPED)

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('dapp')
        verbose_name_plural = _('dapps')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        # TODO remove app from deployement and remove all files related to it when deleting
        super().delete(*args, **kwargs)

    def deploy(self):
        """One of the function to overwrite when inheriting"""
        pass


class EnvVar(models.Model):
    dapp = models.ForeignKey(Dapp, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    value = models.CharField(max_length=8192)

    class Meta:
        verbose_name = _('environment variable')
        verbose_name_plural = _('environment variables')

    def __str__(self):
        return self.name


class Build(models.Model):
    number = models.PositiveIntegerField(default=1)
    is_success = models.BooleanField(null=True)
    is_deployed = models.BooleanField(default=False)
    logs = models.TextField()
    source = models.FilePathField(null=True)
    bundle = models.FilePathField(null=True)

    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _('build')
        verbose_name_plural = _('builds')

    def __str__(self):
        return self.number
