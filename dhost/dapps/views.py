from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildsViewSet,
                                BundleViewSet, EnvironmentVariableViewSet)

from .models import Dapp
from .serializers import AbstractDeploymentSerializer, DappSerializer


class DappViewSet(BuildOptionsViewSet):
    serializer_class = DappSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        """Add `owner` when creating the dapp"""
        data = request.data.copy()
        data.update({'owner': self.request.user.id})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def get_queryset(self):
        """Filter user's apps"""
        user = self.request.user
        return Dapp.objects.filter(owner=user)

    @action(detail=True, methods=['get'])
    def deploy(self, request, pk=None):
        dapp = self.get_object()
        is_success = dapp.deploy()
        if is_success:
            return Response({'status': 'deployment successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AbstractDeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AbstractDeploymentSerializer


class DappBundleViewSet(BundleViewSet):
    pass


class DappBuildsViewSet(BuildsViewSet):
    pass


class DappEnvironmentVariableViewSet(EnvironmentVariableViewSet):
    pass
