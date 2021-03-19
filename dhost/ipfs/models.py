from django.db import models
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import AbstractDeployment, Dapp


class IPFSDapp(Dapp):
    """Dapp raidy to be deployed to the IPFS network"""

    hash = models.CharField(_('IPFS hash'), max_length=128, blank=True)

    class Meta(Dapp.Meta):
        verbose_name = _('IPFS Dapp')
        verbose_name_plural = _('IPFS Dapps')

    def deploy(self, bundle):
        """Create an IPFSDeployment object and deploy it"""
        pass

    def _get_url(self):
        """Generate URL based on hash and IPFS gateway"""
        pass


class IPFSDeployment(AbstractDeployment):
    hash = models.CharField(_('IPFS hash'), max_length=128, blank=True)

    class Meta(AbstractDeployment.Meta):
        verbose_name = _('IPFS Deployment')
        verbose_name_plural = _('IPFS Deployments')

    def delete(self, *args, **kwargs):
        # TODO remove from IPFS
        super().delete(*args, **kwargs)
