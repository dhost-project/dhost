from rest_framework import viewsets

from dhost.builds.views import BuildOptionsViewSet

from .models import Dapp
from .serializers import AbstractDeploymentSerializer, DappSerializer


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer


class AbstractDeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AbstractDeploymentSerializer
