from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.builds.models import BuildOptions


class AbstractDapp(models.Model):
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
        verbose_name=_('owner'),
        related_name="%(class)ss",
        related_query_name="%(class)ss",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(unique=True, blank=True, null=True)
    url = models.CharField(_('URL'), max_length=2048, blank=True)

    class Statuses(models.TextChoices):
        """All the different statuses a Dapp can be in:
          - STOPED: When the Dapp is neither UP nor UNAVAILABLE nor doing any
            other change in state
          - BUILDING: In the process of building the bundle
          - BUILT: When the source is bundled
          - DEPLOYING: In the process of deploying
          - STARTING: When the site is deployed but not yet reachable from the
            web (404)
          - UP: When the site is deployed and reachable from the web (200)
          - UNAVAILABLE: When the site should be reachable but is not for a
            technical reason
          - ERROR: Error while trying to retrieve the state of the Dapp
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

    created_at = models.DateTimeField(_('created'), default=timezone.now)

    class Meta:
        verbose_name = _('dapp')
        verbose_name_plural = _('dapps')
        abstract = True

    def __str__(self):
        return self.name

    def build(self):
        """One of the function to overwrite when inheriting"""
        raise Exception("The build process is not implemented.")

    def deploy(self):
        """One of the function to overwrite when inheriting"""
        raise Exception("The deployment process is not implemented.")


class Dapp(AbstractDapp, BuildOptions):
    """A fully functionnal Dapp with options and ability to build from
    options
    """

    class Meta(AbstractDapp.Meta):
        pass


class Bundle(models.Model):
    """Bundled web app raidy for deployment"""

    dapp = models.ForeignKey(
        Dapp,
        on_delete=models.CASCADE,
        related_name='bundles',
        related_query_name='bundles',
        verbose_name=_('dapp'),
    )
    build = models.ForeignKey(
        'builds.Build',
        on_delete=models.SET_NULL,
        null=True,
        related_name='bundles',
        related_query_name='bundles',
        blank=True,
        verbose_name=_('build'),
    )
    folder = models.FilePathField(
        _('folder'),
        null=True,
        blank=True,
        allow_files=True,
        allow_folders=True,
    )
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = _('bundle')
        verbose_name_plural = _('bundles')


class AbstractDeployment(models.Model):
    """Model representing a single deployment process"""

    dapp = None
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

    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)

    class Meta:
        verbose_name = _('deployment')
        verbose_name_plural = _('deployments')
        abstract = True

    def __str__(self):
        if self.bundle:
            return str(self.bundle)
        else:
            return str(self.dapp)
