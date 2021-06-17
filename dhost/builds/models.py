import os
import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Bundle

from .build_service import BuildService


def source_path():
    return os.path.join(settings.MEDIA_ROOT, 'source')


class BuildOptions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.FilePathField(
        null=True,
        blank=True,
        path=source_path,
        recursive=True,
        allow_files=True,
        allow_folders=True,
        max_length=1024,
        verbose_name=_('Source folder'),
    )
    command = models.CharField(
        _('build command'),
        max_length=2048,
        blank=True,
        help_text=_('Command used during the build process.'),
    )
    docker = models.CharField(
        max_length=128,
        blank=True,
        help_text=_('Container used for the build process.'),
    )

    class Meta:
        verbose_name = _('build options')
        verbose_name_plural = _('builds options')

    def __str__(self):
        return '{} ({})'.format(self.docker, self.command)

    def build(self):
        """Create a `Build` object and start the building process from the
        source in the Docker container specified in `docker_container` and with
        the command
        """
        build = Build(options=self, source_path=self.source)
        build.save()
        is_success, bundle = build.build()
        return is_success, bundle


class Build(models.Model):
    """A single build instance"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    options = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name='builds',
        related_query_name='builds',
    )
    is_success = models.BooleanField(
        null=True,
        blank=True,
        help_text=_('Based on the build return code'),
    )
    logs = models.TextField(
        blank=True,
        help_text=_('Raw logs output of the build process'),
    )
    source_path = models.FilePathField(
        null=True,
        blank=True,
        path=source_path,
        recursive=True,
        allow_files=False,
        allow_folders=True,
        max_length=1024,
        help_text=_('Source folder'),
    )
    bundle = models.OneToOneField(
        'dapps.Bundle',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='build',
        related_query_name='build',
        verbose_name=_('bundle'),
    )

    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('build')
        verbose_name_plural = _('builds')

    def delete(self, *args, **kwargs):
        # TODO remove source when deleting a build if and only if unused in
        # `BuildOptions`, this would mean that it's not the current build
        # source
        super().delete(*args, **kwargs)

    def __str__(self):
        return 'build:{}'.format(self.id.hex[:7])

    def build(self):
        """
        return:
          - BOOL: success status, True if succeed
          - BUNDLE (object): if succeed then the Bundle object is created

        Start the build process, when it's done and if the build succeed
        create a `Bundle` object containing the static files generated during
        the build process
        """
        bundle_path_var = self.start_build()
        if self.is_success:
            bundle = Bundle.objects.create(
                options=self.options,
                folder=bundle_path_var,
            )
            bundle.save()
            self.bundle = bundle
            self.save()
        return self.is_success, self.bundle

    def start_build(self):
        container = self.options.docker
        source_path = self.source_path
        command = self.options.command
        self.start = timezone.now()

        # Generate dict of the environment variables
        envvars = {}
        for var_object in self.options.envvars.all():
            envvars[var_object.variable] = var_object.value

        build_service = BuildService(
            container=container,
            source_path=source_path,
            command=command,
            envvars=envvars,
        )
        return build_service.build()

    def stop_build(self, is_success=False, logs=None):
        self.is_success = is_success
        self.logs = logs
        self.end = timezone.now()
        self.save()


class EnvVar(models.Model):
    options = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name='envvars',
        related_query_name='envvars',
    )
    variable = models.SlugField(max_length=1024)
    value = models.CharField(max_length=8192)

    class Meta:
        verbose_name = _('environment variable')
        verbose_name_plural = _('environment variables')
        constraints = [
            models.UniqueConstraint(fields=['options', 'variable'],
                                    name='unique variable'),
        ]

    def __str__(self):
        return '{}={}'.format(self.variable, self.value)
