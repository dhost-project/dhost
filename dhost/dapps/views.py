from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildViewSet,
                                BundleViewSet, EnvVarViewSet)
from dhost.github.views import BranchViewSet, RepositoryViewSet
from dhost.logs.views import APILogViewSet

from .models import Dapp, DappGithubRepo, Deployment
from .permissions import DappHasGithubLinked, DappPermission
from .serializers import (DappGithubRepoSerializer, DappReadOnlySerializer,
                          DappSerializer, DeploymentSerializer)


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer
    permission_classes = [DappPermission]
    lookup_field = 'slug'

    def get_queryset(self):
        """Filter user's apps"""
        queryset = super().get_queryset()
        owner = self.request.user
        return queryset.filter(owner=owner)

    def create(self, request):
        # Add `owner` when creating the dapp
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
        # `pk` is replaced by `slug` because the lookup_field changed.
        return super().build(request)


class DappReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A list of every dapps, regardless of wich type they are.
    """

    queryset = Dapp.objects.all()
    serializer_class = DappReadOnlySerializer
    permission_classes = [DappPermission]
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.user
        return queryset.filter(owner=owner)


class DappViewMixin:
    """
    Mixin to handle the nested router wich send an argument with the dapp slug
    used to filter the dapps.
    """
    dapp_model_class = Dapp
    dapp_reverse_name = 'options'
    dapp_url_slug = 'dapp_slug'

    def get_dapp(self):
        owner = self.request.user
        slug = self.kwargs[self.dapp_url_slug]
        return get_object_or_404(self.dapp_model_class, owner=owner, slug=slug)

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


class DappEnvVarViewSet(DappViewMixin, EnvVarViewSet):

    def create(self, request):
        # Auto add `option` (dapp) when creating the envvar
        data = request.data.copy()
        data.update({'option': self.get_dapp()})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class DappAPILogViewSet(DappViewMixin, APILogViewSet):
    pass


class DappGithubRepoViewSet(DappViewMixin, RepositoryViewSet):
    queryset = DappGithubRepo.objects.all()
    serializer_class = DappGithubRepoSerializer
    permission_classes = [DappHasGithubLinked]
    dapp_reverse_name = 'dapp'

    def get_repo(self):
        return get_object_or_404(DappGithubRepo.objects.all(),
                                 dapp=self.get_dapp())

    def list(self, request, dapp_slug):
        repo = self.get_repo()
        serializer = self.get_serializer(repo)
        return Response(serializer.data)


class DappBranchViewSet(DappViewMixin, BranchViewSet):
    dapp_reverse_name = 'dapp'
