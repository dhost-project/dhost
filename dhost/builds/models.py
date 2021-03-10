import os

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def source_path():
    return os.path.join(settings.MEDIAO_DIR, 'source')


def bundle_path():
    return os.path.join(settings.MEDIAO_DIR, 'bundle')


class BuildOptions(models.Model):
    source = models.FilePathField(
        null=True,
        path=source_path,
        recursive=True,
        allow_files=False,
        allow_folders=True,
        max_length=1024,
        help_text=_('Source folder'),
    )
    command = models.CharField(
        _('build command'),
        max_length=2048,
        help_text=_('Command used during the build process.'),
    )
    docker_container = models.CharField(
        max_length=128,
        blank=True,
        help_text=_('Container used for the build process'),
    )

    class Meta:
        verbose_name = _('build options')
        verbose_name_plural = _('builds options')

    def build(self):
        """Create a `Build` object and start the building process from the
        source in the Docker container specified in `docker_container` and with
        the command
        """
        pass


class Build(models.Model):
    """A single build instance"""

    options = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name='builds',
        related_query_name='builds',
    )
    number = models.PositiveIntegerField(
        default=1,
        help_text=_('Build number'),
    )
    is_success = models.BooleanField(
        null=True,
        help_text=_('Based on the build return code'),
    )
    logs = models.TextField(
        help_text=_('Raw logs output of the build process'),
    )
    source = models.FilePathField(
        null=True,
        path=source_path,
        recursive=True,
        allow_files=False,
        allow_folders=True,
        max_length=1024,
        help_text=_('Source folder'),
    )
    bundle = models.FilePathField(
        null=True,
        path=bundle_path,
        recursive=True,
        allow_files=False,
        allow_folders=True,
        max_length=1024,
        help_text=_('Bundle folder')
    )

    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _('build')
        verbose_name_plural = _('builds')
        unique_together = [['options', 'number']]

    def save(self, *args, **kwargs):
        if not self.id and not self.number:
            self.number = 2
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # TODO remove both source and bundle when deleting a build if and only
        # if unused in BuildOptions, this woul mean that it's not the current
        # build source, and also check if unused in Dapp
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.number

    @property
    def is_deployed(self):
        pass

    def build(self):
        pass

    def stop_building(self):
        pass


class EnvironmentVariable(models.Model):
    options = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name='envars',
    )
    variable = models.CharField(max_length=1024)
    value = models.CharField(max_length=8192)

    class Meta:
        verbose_name = _('environment variable')
        verbose_name_plural = _('environment variables')

    def __str__(self):
        return self.variable
