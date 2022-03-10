from celery import shared_task

from dhost.ipfs.ipfs import IPFSAPI

ipfs = CLUSTERIPFSAPI()


@shared_task
def task_add_file(file_path):
    ipfs_obj = ipfs.add(file_path)
    ##ipfs.pin_add(arg=ipfs_obj["Hash"]) Le pin se fait automatiquement


@shared_task
def task_remove_file(CID):
    ipfs.unpinCID(CID)
