import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.builds.models import BuildOptions, Bundle
from dhost.github.models import Branch, Repository


class Dapp(BuildOptions):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        related_name="%(app_label)s_%(class)s",
        related_query_name="%(app_label)s_%(class)s",
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(_('dapp name'), max_length=256,
                            help_text='[A-Za-z0-9_-]')
    url = models.CharField(_('URL'), max_length=2048, blank=True)

    class Statuses(models.TextChoices):
        """
        All the different statuses a Dapp can be in:
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
        constraints = [
            models.UniqueConstraint(fields=['owner', 'slug'],
                                    name='%(app_label)s_%(class)s_unique_slug'),
        ]

    def __str__(self):
        return self.slug

    def deploy(self, bundle=None):
        """Create an `IPFSDeployment` object and start the deployment process
        from the bundled files
        """
        if bundle is None and len(self.bundles.all()) > 0:
            bundle = self.bundles.all()[0]

        deployment = self.create_deployment(bundle)
        deployment.save()
        is_success = deployment.deploy()
        return is_success

    def create_deployment(self, bundle=None):
        """Return a specific application deployment instance"""
        raise NotImplementedError

    def get_dapp_type(self):
        """Return the available dapp implementation."""
        if hasattr(self, 'ipfsdapp'):
            return 'ipfs'
        return None


class Deployment(models.Model):
    """Model representing a single deployment process"""

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

    def deploy(self):
        raise NotImplementedError


class DappGithubRepo(models.Model):
    """
    Represent the link between a Dapp and a Github repository, it also add some
    options related to the deployment `auto_deploy` specifies if the Dapp
    should be re-deployed when a webhook linked to that repo is called.
    """
    dapp = models.OneToOneField(
        Dapp,
        related_name='github_repo',
        related_query_name='github_repo',
        on_delete=models.CASCADE,
    )
    repo = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
    )
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    auto_deploy = models.BooleanField(
        default=False,
        help_text=_('Automaticaly deploy the dapp when a webhook is called.'),
    )
    confirm_ci = models.BooleanField(
        default=False,
        help_text=_('Wait for CI to be done before deploying the dapp when'
                    'auto deploy is on.'),
    )

    class Meta:
        verbose_name = _('Dapp Github repository')
        verbose_name_plural = _('Dapp Github repositories')
