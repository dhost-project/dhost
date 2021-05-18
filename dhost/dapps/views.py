from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.builds.views import BuildOptionsViewSet

from .models import Dapp
from .serializers import AbstractDeploymentSerializer, DappSerializer


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer

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
