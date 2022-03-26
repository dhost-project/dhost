from celery import shared_task

from dhost.ipfs.ipfs import ClusterIPFSAPI

ipfs = ClusterIPFSAPI()


@shared_task
def task_add_file(file_path):
    ipfs.add(file_path)
    # ipfs.pin_add(arg=ipfs_obj["Hash"]) Le pin se fait automatiquement


@shared_task
def task_remove_file(CID):
    ipfs.unpin_cid(CID)
