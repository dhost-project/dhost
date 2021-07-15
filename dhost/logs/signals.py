from crum import get_current_user
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from dhost.builds.models import (Build, BuildOptions, EnvVar, build_fail,
                                 build_success, post_build_start)
from dhost.dapps.models import Bundle, Dapp
from dhost.github.models import GithubOptions
from dhost.ipfs.models import IPFSDapp

from .models import ActionFlags, APILog


def log_action(instance, action_flag, dapp, user=None):
    """Log an action on a dapp."""
    APILog.objects.log_action(user=user,
                              obj=instance,
                              action_flag=action_flag,
                              dapp=dapp)


def log_with_user(instance, action_flag, dapp):
    """Log with the current user."""
    user = get_current_user()
    log_action(instance=instance, action_flag=action_flag, dapp=dapp, user=user)


@receiver(post_save, sender=Dapp)
@receiver(post_save, sender=IPFSDapp)
def log_dapp_create_or_update(sender, instance, created, **kwargs):
    if created:
        action_flag = ActionFlags.DAPP_ADDITION
    else:
        action_flag = ActionFlags.DAPP_CHANGE
    log_with_user(instance=instance, action_flag=action_flag, dapp=instance)


@receiver(post_save, sender=Bundle)
def log_bundle_create(sender, instance, created, **kwargs):
    if created:
        log_with_user(instance=instance,
                      action_flag=ActionFlags.BUNDLE_ADDITION,
                      dapp=instance.dapp)


@receiver(post_delete, sender=Bundle)
def log_bundle_delete(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.BUNDLE_DELETION,
                  dapp=instance.dapp)


@receiver(post_save, sender=BuildOptions)
def log_build_options_create_or_update(sender, instance, created, **kwargs):
    if created:
        action_flag = ActionFlags.BUILD_OPTIONS_ADDITION
    else:
        action_flag = ActionFlags.BUILD_OPTIONS_CHANGE
    log_with_user(instance=instance,
                  action_flag=action_flag,
                  dapp=instance.dapp)


@receiver(post_delete, sender=BuildOptions)
def log_build_options_delete(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.BUILD_OPTIONS_DELETION,
                  dapp=instance.dapp)


@receiver(post_save, sender=EnvVar)
def log_env_var_create_or_update(sender, instance, created, **kwargs):
    if created:
        action_flag = ActionFlags.ENV_VAR_ADDITION
    else:
        action_flag = ActionFlags.ENV_VAR_CHANGE
    log_with_user(instance=instance,
                  action_flag=action_flag,
                  dapp=instance.buildoptions.dapp)


@receiver(post_delete, sender=EnvVar)
def log_env_var_delete(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.ENV_VAR_DELETION,
                  dapp=instance.buildoptions.dapp)


@receiver(post_save, sender=GithubOptions)
def log_github_options_create_or_update(sender, instance, created, **kwargs):
    if created:
        action_flag = ActionFlags.GITHUB_OPTIONS_ADDITION
    else:
        action_flag = ActionFlags.GITHUB_OPTIONS_CHANGE
    log_with_user(instance=instance,
                  action_flag=action_flag,
                  dapp=instance.dapp)


@receiver(post_delete, sender=GithubOptions)
def log_github_options_delete(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.GITHUB_OPTIONS_DELETION,
                  dapp=instance.dapp)


@receiver(post_build_start, sender=BuildOptions)
def log_build_start(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.BUILD_START,
                  dapp=instance.buildoptions.dapp)


@receiver(build_success, sender=Build)
def log_build_success(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.BUILD_SUCCESS,
                  dapp=instance.buildoptions.dapp)


@receiver(build_fail, sender=Build)
def log_build_fail(sender, instance, **kwargs):
    log_with_user(instance=instance,
                  action_flag=ActionFlags.BUILD_FAIL,
                  dapp=instance.buildoptions.dapp)
