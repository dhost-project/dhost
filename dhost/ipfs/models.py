import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from dhost.dapps.models import Dapp, Deployment

from .ipfs import CLUSTERIPFSAPI

import json


class IPFSDeployment(Deployment):
    ipfs_hash = models.CharField(_("IPFS hash"), max_length=128, blank=True)

    class Meta:
        verbose_name = _("IPFS Deployment")
        verbose_name_plural = _("IPFS Deployments")

    def delete(self, *args, **kwargs):
        # TODO remove from IPFS
        super().delete(*args, **kwargs)

    def deploy(self,url):
        # deploying on the IPFS
        ipfs = CLUSTERIPFSAPI()
        result = ipfs.add(url)
        print("ADD--> ", result, type(result))
        list_raw_data = str(result).split("\\n")
        first_json = json.loads(list_raw_data[0].replace("b'",""))
        self.ipfs_hash=first_json["cid"]["/"]
        self.save()

class IPFSDapp(Dapp):
    """Dapp raidy to be deployed to the IPFS network."""

    ipfs_hash = models.CharField(_("IPFS hash"), max_length=128, blank=True)
    ipfs_gateway = models.URLField(
        _("IPFS public gateway"),
        default="https://ipfs.io/ipfs/",
        null=True,
        blank=True,
    )
    deployment_class = IPFSDeployment

    class Meta:
        verbose_name = _("IPFS Dapp")
        verbose_name_plural = _("IPFS Dapps")

    def get_public_url(self):
        """Generate public URL based on hash and IPFS gateway."""
        return "{}{}".format(self.ipfs_gateway, self.ipfs_hash)

    def create_deployment(self, bundle=None):
        new_deploy = IPFSDeployment.objects.create(dapp=self)
        new_deploy.save()
        return new_deploy.deploy(self.url)
        

    


    
