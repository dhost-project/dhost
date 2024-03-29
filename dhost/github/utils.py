from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):
    """Raised if a user account has no Github account linked."""

    def __init__(self, message="Github account not linked."):
        super().__init__(message)


def user_has_github_account(user):
    """Check if the user has a Github account linked.

    Args:
        user (User): User to check.

    Returns:
        bool: If the user has a Github account linked.
    """
    return len(user.social_auth.filter(provider="github")) > 0


def get_user_github_account(user):
    """Get the user's Github social_auth model.

    Args:
        user (User): The user.

    Returns:
        SocialAuth: The user's SocialAuth 'github' object.

    Raises:
        GithubNotLinkedError: Raised if the user's account is not linked.
    """
    try:
        return user.social_auth.get(provider="github")
    except ObjectDoesNotExist:
        raise GithubNotLinkedError()


def get_token_from_github_account(github_account):
    """Get the github_account's `access_token` stored in `extra_data`.

    Args:
        github_account (SocialAuth): A SocialAuth object for Github.

    Returns:
        str: Github API access_token.

    Raise:
        Exception: In case the `access_token` is not present in the github
            account extra_data. This should never happen but it can if for some
            reason the fields was edited.
    """
    if "access_token" not in github_account.extra_data:
        raise Exception(
            "'access_token' missing from github_account.extra_data for "
            "github_account '{}' (id: '{}')".format(
                github_account, github_account.id
            )
        )
    return github_account.extra_data["access_token"]
