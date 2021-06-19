def user_has_github_account(user):
    """Return True if the user has a Github account linked."""
    return len(user.social_auth.filter(provider='github')) > 0


def get_user_github_account(user):
    """
    Return the user's Github social_auth model.
    Note that it will raise an error if the user has no github account linked,
    you should always check if it's the case before.
    """
    return user.social_auth.get(provider='github')
