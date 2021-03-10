from django.db import models
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import AbstractDeployment, Dapp


class IPFSDapp(Dapp):
    """Dapp raidy to be deployed to the IPFS network"""

    hash = models.CharField(_('IPFS hash'), max_length=128, blank=True)

    def deploy(self):
        """Create an IPFSDeployment object and deploy it"""
        pass

    def _get_url(self):
        """Generate URL based on hash and IPFS gateway"""
        pass


class IPFSDeployment(AbstractDeployment):
    dapp = models.ForeignKey(
        IPFSDapp,
        related_name='deployments',
        related_query_name='deployments',
        on_delete=models.CASCADE,
        verbose_name=_('dapp'),
    )
    hash = models.CharField(_('IPFS hash'), max_length=128, blank=True)

    def __str__(self):
        return self.hash

    def delete(self):
        # TODO remove from IPFS
        pass
