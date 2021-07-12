from django.conf import settings
from rest_framework import mixins, viewsets
from rest_framework.metadata import SimpleMetadata
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from dhost import __version__


class APIRootMetadata(SimpleMetadata):

    def determine_metadata(self, request, view):
        metadata = super().determine_metadata(request, view)
        metadata['version'] = __version__
        return metadata


class APIRootView(APIView):
    name = 'API Root'
    description = f'DHost REST API version {__version__}'
    metadata_class = APIRootMetadata
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        """REST API root."""
        data = {
            'dapps':
                reverse_lazy(
                    'api:dapp-list',
                    request=request,
                ),
            'github_repos':
                reverse_lazy(
                    'api:github_repo-list',
                    request=request,
                ),
            'ipfs_dapps':
                reverse_lazy(
                    'api:ipfs_dapp-list',
                    request=request,
                ),
            'notifications':
                reverse_lazy(
                    'api:notification-list',
                    request=request,
                ),
            'applications':
                reverse_lazy(
                    'api:oauth2_application-list',
                    request=request,
                ),
            'tokens':
                reverse_lazy(
                    'api:oauth2_token-list',
                    request=request,
                ),
            'me':
                reverse_lazy(
                    'api:user-me',
                    request=request,
                ),
        }

        if settings.SETTINGS_MODULE == 'dhost.settings.development':
            data.update({
                'doc': reverse_lazy(
                    'api:redoc',
                    request=request,
                ),
                'schema': reverse_lazy(
                    'api:openapi-schema',
                    request=request,
                ),
            })

        return Response(data)


class DestroyListRetrieveViewSet(mixins.DestroyModelMixin,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin,
                                 viewsets.GenericViewSet):
    """A viewset that provides `retrieve`, `destroy`, and `list` actions.

    To use it, override the class and set the `.queryset` and
    `.serializer_class` attributes.
    """

    pass
