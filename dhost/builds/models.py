import os
import uuid

import django.dispatch
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Bundle, Dapp

from .build_service import start_build_service

pre_build_start = django.dispatch.Signal()
post_build_start = django.dispatch.Signal()
build_success = django.dispatch.Signal()
build_fail = django.dispatch.Signal()


def source_path():
    return os.path.join(settings.MEDIA_ROOT, "source")


class BuildOptions(models.Model):
    dapp = models.OneToOneField(
        Dapp,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    source = models.FilePathField(
        null=True,
        blank=True,
        path=source_path,
        recursive=True,
        allow_files=True,
        allow_folders=True,
        max_length=1024,
        verbose_name=_("Source folder"),
    )
    command = models.CharField(
        _("build command"),
        max_length=2048,
        blank=True,
        help_text=_("Command used during the build process."),
    )
    docker = models.CharField(
        max_length=128,
        blank=True,
        help_text=_("Container used for the build process."),
    )

    class Meta:
        verbose_name = _("build options")
        verbose_name_plural = _("builds options")

    def __str__(self):
        return "{} ({})".format(self.docker, self.command)

    def build(self):
        """Create a `Build` object and start the building process.

        From the source in the Docker container specified in `docker_container`
        and with the command.
        """
        build = Build.objects.create(buildoptions=self, source_path=self.source)
        pre_build_start.send(sender=self.__class__, instance=build)
        build.start_build()
        post_build_start.send(sender=self.__class__, instance=build)
        return build


class Build(models.Model):
    """A single build instance."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buildoptions = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name="builds",
        related_query_name="builds",
    )
    is_success = models.BooleanField(
        null=True,
        blank=True,
        help_text=_("Based on the build return code"),
    )
    logs = models.TextField(
        blank=True,
        help_text=_("Raw logs output of the build process"),
    )
    source_path = models.FilePathField(
        null=True,
        blank=True,
        path=source_path,
        recursive=True,
        allow_files=False,
        allow_folders=True,
        max_length=1024,
        help_text=_("Source folder"),
    )
    bundle = models.OneToOneField(
        "dapps.Bundle",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="build",
        related_query_name="build",
        verbose_name=_("bundle"),
    )

    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _("build")
        verbose_name_plural = _("builds")

    def delete(self, *args, **kwargs):
        # TODO remove source when deleting a build if and only if unused in
        # `BuildOptions`, this would mean that it's not the current build
        # source
        super().delete(*args, **kwargs)

    def __str__(self):
        return "build:{}".format(self.id.hex[:7])

    def start_build(self):
        """Start the build process.

        When it's done and if the build succeed, create a `Bundle` object
        containing the static files generated during the build process.
        """
        self.start = timezone.now()
        self.save()

        # Generate dict of the environment variables
        envvars = {}
        for var_object in self.buildoptions.envvars.all():
            envvars[var_object.variable] = var_object.value

        start_build_service(
            container=self.buildoptions.docker,
            source_path=self.source_path,
            command=self.buildoptions.command,
            envvars=envvars,
        )

    def end_build(self, bundle_path, is_success=False, logs=None, error=None):
        """End of build process."""
        self.is_success = is_success
        self.logs = logs
        self.end = timezone.now()
        self.save()

        if is_success:
            Bundle.objects.create(
                dapp=self.buildoptions.dapp, folder=bundle_path
            )
            build_success.send(sender=self.__class__, instance=self)
        else:
            build_fail.send(sender=self.__class__, instance=self, error=error)


class EnvVar(models.Model):
    """Environment variables used during the build process."""

    buildoptions = models.ForeignKey(
        BuildOptions,
        on_delete=models.CASCADE,
        related_name="envvars",
        related_query_name="envvars",
    )
    variable = models.SlugField(max_length=1024)
    value = models.CharField(max_length=8192)
    # hide the value if the variable is sensitive, the user can still write to
    # it, but he shouldn't be able to view it
    sensitive = models.BooleanField(
        default=False,
        help_text=_("Hide the value if set."),
    )

    class Meta:
        verbose_name = _("environment variable")
        verbose_name_plural = _("environment variables")
        constraints = [
            models.UniqueConstraint(
                fields=["buildoptions", "variable"], name="unique variable"
            ),
        ]

    def __str__(self):
        if not self.sensitive:
            return "{}={}".format(self.variable, self.value)
        return self.variable
