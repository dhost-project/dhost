from rest_framework import permissions

from dhost.github.permissions import HasGithubLinked


class DappPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True
        return obj.owner == request.user


class DappHasGithubLinked(HasGithubLinked):

    def has_object_permission(self, request, view, obj):
        return obj.repo.users.filter(id=request.user.id).exists()
