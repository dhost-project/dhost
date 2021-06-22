from django.core.exceptions import ObjectDoesNotExist


class GithubNotLinkedError(Exception):
    """
    Raised if a user account has no Github account linked (`social_auth`).
    """

    def __init__(self, message="Github account not linked."):
        super().__init__(message)


def user_has_github_account(user):
    """Return True if the user has a Github account linked."""
    return len(user.social_auth.filter(provider='github')) > 0


def get_user_github_account(user):
    """
    Return the user's Github social_auth model.
    Note that it will raise a custom error if the user has no github account
    linked, you should always check if it's the case before.
    """
    try:
        return user.social_auth.get(provider='github')
    except ObjectDoesNotExist:
        raise GithubNotLinkedError()


def get_token_from_github_account(github_account):
    """
    Return the github_account's `access_token` stored in `extra_data`.
    Raise an exceptions if it's not present in the `extra_data`, this in theory
    should never happen, but it can if for some reason the fields has been
    edited.
    """
    if 'access_token' not in github_account.extra_data:
        raise Exception(
            "'access_token' missing from github_account.extra_data for "
            "github_account '{}' (id: '{}')".format(github_account,
                                                    github_account.id))
    return github_account.extra_data['access_token']
