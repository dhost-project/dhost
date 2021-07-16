from crum import get_current_user

from .models import APILog


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
