from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings

from dhost.ipfs.ipfs import ClusterIPFSAPI

from dhost.dapps.models import Bundle

from dhost.ipfs.models import IPFSDapp, IPFSDeployment

import os

import shutil

ipfs = ClusterIPFSAPI()
IPFS_MEDIAS = settings.IPFS_MEDIAS


@receiver(post_delete, sender=Bundle)
def remove_local_folder_bundle_delete(sender, instance, **kwargs):
    # Delete bundle folder when deleting the object
    ipfs_local = IPFS_MEDIAS + instance.dapp.slug
    if os.path.exists(ipfs_local):
        shutil.rmtree(ipfs_local)


@receiver(post_delete, sender=IPFSDapp)
def remove_ipfs_folder_dapp_delete(sender, instance, **kwargs):
    # Unpin CID and call garbage collector when deleting the object
    try:
        if instance.ipfs_hash:
            ipfs.unpin_cid(instance.ipfs_hash)
            ipfs.call_garbage_collector()
    except:
        pass
