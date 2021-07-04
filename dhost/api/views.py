from django.urls import reverse
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
            'me': reverse('api:users-me'),
        }
        return Response(data)


class APIv1RootView(APIRootView):
    pass
