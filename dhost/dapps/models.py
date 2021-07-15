import os
import uuid

import django.dispatch
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .utils import get_dapp_type

pre_deploy_start = django.dispatch.Signal()
post_deploy_start = django.dispatch.Signal()
deploy_success = django.dispatch.Signal()
deploy_fail = django.dispatch.Signal()


def bundle_path():
    return os.path.join(settings.MEDIA_ROOT, 'bundle')


class Dapp(models.Model):
    slug = models.SlugField(
        _('dapp name'),
        primary_key=True,
        max_length=256,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        related_name="%(app_label)s_%(class)s",
        related_query_name="%(app_label)s_%(class)s",
        on_delete=models.CASCADE,
    )
    url = models.CharField(_('URL'), max_length=2048, blank=True)

    class Statuses(models.TextChoices):
        """All the different statuses a Dapp can be in.

        Choices:
          * STOPED: When the Dapp is neither UP nor UNAVAILABLE nor doing any
            other change in state
          * BUILDING: In the process of building the bundle
          * BUILT: When the source is bundled
          * DEPLOYING: In the process of deploying
          * STARTING: When the site is deployed but not yet reachable from the
            web (404)
          * UP: When the site is deployed and reachable from the web (200)
          * UNAVAILABLE: When the site should be reachable but is not for a
            technical reason
          * ERROR: Error while trying to retrieve the state of the Dapp
        """

        STOPED = 'SO', _('Stoped')
        BUILDING = 'BI', _('Building')
        BUILT = 'BT', _('Builed')
        DEPLOYING = 'DP', _('Deploying')
        STARTING = 'SA', _('Starting')
        UP = 'UP', _('Running')
        UNAVAILABLE = 'UA', _('Unavailable')
        ERROR = 'ER', _('Error')

    status = models.CharField(
        _('status'),
        max_length=2,
        choices=Statuses.choices,
        default=Statuses.STOPED,
    )

    created_at = models.DateTimeField(_('created at'), default=timezone.now)

    deployment_class = None

    class Meta:
        verbose_name = _('dapp')
        verbose_name_plural = _('dapps')

    def __str__(self):
        return self.slug

    def deploy(self, bundle=None, **kwargs):
        """Deploy the dapp.

        Create an `IPFSDeployment` object and start the deployment process
        from the bundled files.
        """
        if bundle is None and len(self.bundles.all()) > 0:
            bundle = self.bundles.all()[0]

        deployment = self.deployment_class.objects.create(dapp=self,
                                                          bundle=bundle,
                                                          **kwargs)
        deployment.start_deploy()

    def create_deployment(self, bundle=None):
        """Return a specific application deployment instance."""
        raise NotImplementedError

    def get_dapp_type(self):
        return get_dapp_type(self)


class Bundle(models.Model):
    """Bundled web app raidy for deployment."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dapp = models.ForeignKey(
        Dapp,
        on_delete=models.CASCADE,
        related_name='bundles',
        related_query_name='bundles',
    )
    folder = models.FilePathField(
        _('folder'),
        null=True,
        blank=True,
        path=bundle_path,
        allow_files=True,
        allow_folders=True,
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('bundle')
        verbose_name_plural = _('bundles')

    def __str__(self):
        return 'bundl:{}'.format(self.id.hex[:7])

    def delete(self, *args, **kwargs):
        # TODO delete bundle folder when deleting the object
        super().delete(*args, **kwargs)


class Deployment(models.Model):
    """Model representing a single deployment process."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dapp = models.ForeignKey(
        Dapp,
        related_name='deployments',
        related_query_name='deployments',
        on_delete=models.CASCADE,
        null=True,
    )
    bundle = models.ForeignKey(
        Bundle,
        related_name='deployments',
        related_query_name='deployments',
        on_delete=models.CASCADE,
        null=True,
    )

    class Statuses(models.TextChoices):
        STOPED = 'SO', _('Stoped')
        DEPLOYING = 'DP', _('Deploying')
        STARTING = 'SA', _('Starting')
        UP = 'UP', _('Running')
        UNAVAILABLE = 'UA', _('Unavailable')

    status = models.CharField(
        max_length=2,
        choices=Statuses.choices,
        default=Statuses.STOPED,
    )

    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('deployment')
        verbose_name_plural = _('deployments')

    def __str__(self):
        return 'dplmt:{}'.format(self.id.hex[:7])

    def start_deploy(self):
        pre_deploy_start.send(sender=self.__class__, instance=self)
        self.deploy()
        post_deploy_start.send(sender=self.__class__, instance=self)

    def deploy(self):
        raise NotImplementedError

    def end_deploy(self, is_success=False):
        if is_success:
            deploy_success.send(sender=self.__class__, instance=self)
        else:
            deploy_fail.send(sender=self.__class__, instance=self)
