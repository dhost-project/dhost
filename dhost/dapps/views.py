from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildViewSet,
                                BundleViewSet, EnvironmentVariableViewSet)

from .models import Dapp, Deployment
from .permissions import DappPermission
from .serializers import DappSerializer, DeploymentSerializer


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer
    permission_classes = [DappPermission]

    def get_queryset(self):
        """Filter user's apps"""
        owner = self.request.user
        return Dapp.objects.filter(owner=owner)

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

    @action(detail=True, methods=['get'])
    def deploy(self, request, pk=None):
        dapp = self.get_object()
        is_success = dapp.deploy()
        if is_success:
            return Response({'status': 'deployment successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


class DappDeploymentViewSet(DeploymentViewSet):
    pass


class DappBundleViewSet(BundleViewSet):
    pass


class DappBuildViewSet(BuildViewSet):
    pass


class DappEnvironmentVariableViewSet(EnvironmentVariableViewSet):
    pass
