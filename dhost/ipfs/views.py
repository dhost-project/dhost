from dhost.dapps.views import (DappAPILogViewSet, DappBranchViewSet,
                               DappBuildViewSet, DappBundleViewSet,
                               DappDeploymentViewSet, DappEnvVarViewSet,
                               DappGithubRepoViewSet, DappViewSet)

from .models import IPFSDapp, IPFSDeployment
from .serializers import IPFSDappSerializer, IPFSDeploymentSerializer


class IPFSDappViewSet(DappViewSet):
    queryset = IPFSDapp.objects.all()
    serializer_class = IPFSDappSerializer


class IPFSDappViewMixin:
    dapp_model_class = IPFSDapp


class IPFSDeploymentViewSet(IPFSDappViewMixin, DappDeploymentViewSet):
    queryset = IPFSDeployment.objects.all()
    serializer_class = IPFSDeploymentSerializer


class IPFSDappBundleViewSet(IPFSDappViewMixin, DappBundleViewSet):
    pass


class IPFSDappBuildViewSet(IPFSDappViewMixin, DappBuildViewSet):
    pass


class IPFSDappEnvVarViewSet(IPFSDappViewMixin, DappEnvVarViewSet):
    pass


class IPFSDappAPILogViewSet(IPFSDappViewMixin, DappAPILogViewSet):
    pass


class IPFSDappGithubRepoViewSet(IPFSDappViewMixin, DappGithubRepoViewSet):
    pass


class IPFSDappBranchViewSet(IPFSDappViewMixin, DappBranchViewSet):
    pass
