from crum import get_current_user
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from dhost.dapps.models import Bundle, Dapp
from dhost.ipfs.models import IPFSDapp

from .models import ActionFlags, APILog


def log_action(instance, action_flag, dapp, user=None):
    APILog.objects.log_action(user=user,
                              obj=instance,
                              action_flag=action_flag,
                              dapp=dapp)


def log_with_user(instance, action_flag, dapp, **kwargs):
    user = get_current_user()
    log_action(instance=instance, action_flag=action_flag, dapp=dapp, user=user)


@receiver(post_save, sender=Dapp)
@receiver(post_save, sender=IPFSDapp)
def log_dapp_create_or_update(sender, instance, created, **kwargs):
    if created:
        action_flag = ActionFlags.DAPP_ADDITION
    else:
        action_flag = ActionFlags.DAPP_CHANGE
    log_with_user(action_flag=action_flag,
                  dapp=instance,
                  instance=instance,
                  **kwargs)


@receiver(post_save, sender=Bundle)
def log_bundle_create(sender, instance, created, **kwargs):
    dapp = instance.dapp
    if created:
        if sender == Bundle:
            action_flag = ActionFlags.BUNDLE_ADDITION
    log_with_user(instance=instance, action_flag=action_flag, dapp=dapp)


@receiver(post_delete, sender=Bundle)
def log_bundle_delete(sender, instance, **kwargs):
    dapp = instance.dapp
    if sender == Bundle:
        action_flag = ActionFlags.BUNDLE_DELETION
    log_with_user(instance=instance, action_flag=action_flag, dapp=dapp)
