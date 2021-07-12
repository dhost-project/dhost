from django.db.models.signals import post_save
from django.dispatch import receiver

from dhost.dapps.models import Dapp
from dhost.ipfs.models import IPFSDapp

from .models import ActionFlags, APILog


@receiver(post_save, sender=Dapp)
@receiver(post_save, sender=IPFSDapp)
def dapp_created(sender, instance, created, **kwargs):
    if created:
        APILog.objects.log_action(
            user=instance.owner,
            obj=instance,
            action_flag=ActionFlags.DAPP_ADDITION,
            dapp=instance,
        )
    else:
        APILog.objects.log_action(
            # TODO get user form request
            user=instance.owner,
            obj=instance,
            action_flag=ActionFlags.DAPP_CHANGE,
            dapp=instance,
        )
