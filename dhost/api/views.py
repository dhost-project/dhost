from django.urls import reverse
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """REST API root."""
        data = {
            'dapps': reverse('api:dapps-list'),
            'github_repos': reverse('api:github_repos-list'),
            'ipfs_dapps': reverse('api:ipfs_dapps-list'),
            'notifications': reverse('api:notifications-list'),
            'me': reverse('api:users-me'),
        }
        return Response(data)


class APIv1RootView(APIRootView):
    pass


class DestroyListRetrieveViewSet(mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """A viewset that provides `retrieve`, `destroy`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass
