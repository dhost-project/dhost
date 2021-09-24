import time

from celery import shared_task


@shared_task
def build(container, source_path, command, envvars):
    print("Build started with:")
    print(f"    container   = {container}")
    print(f"    source_path = {source_path}")
    print(f"    command     = {command}")
    print(f"    envvars     = {envvars}")
    time.sleep(10)
    print("Build ended")
    return True
