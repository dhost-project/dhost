from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildViewSet,
                                BundleViewSet, EnvironmentVariableViewSet)
from dhost.logs.views import DashboardLogEntryViewSet

from .models import Dapp, Deployment
from .permissions import DappPermission
from .serializers import DappSerializer, DeploymentSerializer


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer
    permission_classes = [DappPermission]
    lookup_field = 'slug'

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
    def deploy(self, request, slug=None):
        dapp = self.get_object()
        is_success = dapp.deploy()
        if is_success:
            return Response({'status': 'deployment successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['get'])
    def build(self, request, slug=None):
        return super().build(request)


class DappViewMixin:
    """
    Mixin to handle the nested router wich send an argument with the dapp slug
    used to filter the dapps.
    """
    dapp_reverse_name = 'options'
    dapp_url_slug = 'dapp_slug'

    def get_dapp(self):
        owner = self.request.user
        slug = self.kwargs[self.dapp_url_slug]
        return Dapp.objects.get(owner=owner, slug=slug)

    def get_queryset(self):
        dapp = self.get_dapp()
        filter_kwargs = {self.dapp_reverse_name: dapp}
        return super().get_queryset().filter(**filter_kwargs)


class DeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


class DappDeploymentViewSet(DappViewMixin, DeploymentViewSet):
    pass


class DappBundleViewSet(DappViewMixin, BundleViewSet):
    pass


class DappBuildViewSet(DappViewMixin, BuildViewSet):
    pass


class DappEnvironmentVariableViewSet(DappViewMixin, EnvironmentVariableViewSet):
    pass


class DappDashboardLogEntryViewSet(DappViewMixin, DashboardLogEntryViewSet):
    pass
