from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildViewSet,
                                BundleViewSet, EnvironmentVariableViewSet)

from .models import Dapp, Deployment
from .permissions import DappPermission
from .serializers import DappSerializer, DeploymentSerializer

User = get_user_model()


class DappViewMixin:
    """
    Allow complex URL paths such has `<str:username>/<str:dapp__slug>/` also
    add the permissions of objects based on the "base" dapp permissions
    """
    permission_classes = [DappPermission]
    dapp_url_kwargs = 'dapp__slug'

    def get_dapp_queryset(self):
        """Filter user's apps"""
        if 'username' in self.kwargs:
            owner = get_object_or_404(User.objects.all(),
                                      username=self.kwargs['username'])
        else:
            owner = self.request.user
        return Dapp.objects.filter(owner=owner)

    def get_queryset(self):
        queryset = super().get_queryset()
        dapp_queryset = self.get_dapp_queryset().values_list('id')
        queryset.filter(options__in=dapp_queryset)
        return queryset

    def get_dapp(self):
        """
        Get a single dapp (the current dapp)
        Like get_object but for dapp, using the dapp slug.
        """
        queryset = self.get_dapp_queryset()
        filter_kwargs = {'slug': self.kwargs[self.dapp_url_kwargs]}
        # if the username is given in the URL (<str:username>) it will be used
        # to filter the available objects
        if 'username' in self.kwargs:
            user = get_object_or_404(User.objects.all(),
                                     username=self.kwargs['username'])
            filter_kwargs.update({'owner': user})
        dapp = get_object_or_404(queryset, **filter_kwargs)
        return dapp

    def get_object(self):
        dapp = self.get_dapp()
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        queryset = self.filter_queryset(self.get_queryset())
        filter_kwargs = {
            'options': dapp.id,
            self.lookup_field: self.kwargs[lookup_url_kwarg],
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class DappViewSet(DappViewMixin, BuildOptionsViewSet):
    serializer_class = DappSerializer

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
        return self.get_dapp_queryset()

    def get_object(self):
        return self.get_dapp()

    @action(detail=True, methods=['get'])
    def deploy(self, request, pk=None, *args, **kwargs):
        dapp = self.get_object()
        is_success = dapp.deploy()
        if is_success:
            return Response({'status': 'deployment successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def build(self, request, pk=None, *args, **kwargs):
        return super().build(request, pk=pk)


class DeploymentViewSet(DappViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


class DappBundleViewSet(DappViewMixin, BundleViewSet):
    pass


class DappBuildViewSet(DappViewMixin, BuildViewSet):
    pass


class DappEnvironmentVariableViewSet(DappViewMixin, EnvironmentVariableViewSet):
    pass
