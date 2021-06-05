from rest_framework import permissions


class HasGithubLinked(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # if the user has linked his account with Github
            if len(request.user.social_auth.filter(provider='github')) > 0:
                return True
        return False

    def has_object_permission(self, request, view, obj):
        # user's social_auth object must be the owner of the Github repo
        return obj.owner == request.user.social_auth.get(provider='github')
