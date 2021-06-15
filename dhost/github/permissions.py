from rest_framework import permissions


class HasGithubLinked(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # if the user has linked his account with Github
            if len(request.user.social_auth.filter(provider='github')) > 0:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        return obj.users.filter(id=request.user.id).exists()
