from rest_framework import viewsets

from dhost.dapps.views import DappViewSet

from .models import IPFSDapp, IPFSDeployment
from .serializers import IPFSDappSerializer, IPFSDeploymentSerializer


class IPFSDappViewSet(DappViewSet):
    queryset = IPFSDapp.objects.all()
    serializer_class = IPFSDappSerializer


class IPFSDeploymentViewSet(viewsets.ModelViewSet):
    queryset = IPFSDeployment.objects.all()
    serializer_class = IPFSDeploymentSerializer
