from rest_framework import permissions

from .utils import user_has_github_account


class HasGithubLinked(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # if the user has linked his account with Github
            if user_has_github_account(request.user):
                return True
        return False
