from django.urls import reverse
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from dhost import __version__


class APIRootView(APIView):
    name = 'API Root'
    description = f'DHost REST API version {__version__}'

    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """REST API root."""
        data = {
            'dapps': reverse('api:dapp-list'),
            'github_repos': reverse('api:github_repo-list'),
            'ipfs_dapps': reverse('api:ipfs_dapp-list'),
            'notifications': reverse('api:notification-list'),
            'applications': reverse('api:oauth2_application-list'),
            'tokens': reverse('api:oauth2_token-list'),
            'me': reverse('api:user-me'),
        }
        return Response(data)


class APIv1RootView(APIRootView):
    name = 'API v1 Root'


class DestroyListRetrieveViewSet(mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """A viewset that provides `retrieve`, `destroy`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass
