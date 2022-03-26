from dhost.builds.views import BuildOptionsViewSet, BuildViewSet, EnvVarViewSet
from dhost.dapps.views import BundleViewSet, DappViewSet, DeploymentViewSet
from dhost.github.views import GithubOptionsViewSet
from dhost.logs.views import DappLogViewSet

from .models import IPFSDapp, IPFSDeployment
from .serializers import IPFSDappSerializer, IPFSDeploymentSerializer


class IPFSDappViewSet(DappViewSet):
    queryset = IPFSDapp.objects.all()
    serializer_class = IPFSDappSerializer


class IPFSDappViewMixin:
    dapp_model_class = IPFSDapp


class IPFSDeploymentViewSet(IPFSDappViewMixin, DeploymentViewSet):
    queryset = IPFSDeployment.objects.all()
    serializer_class = IPFSDeploymentSerializer


class IPFSDappBundleViewSet(IPFSDappViewMixin, BundleViewSet):
    pass


class IPFSDappBuildOptionsViewSet(IPFSDappViewMixin, BuildOptionsViewSet):
    pass


class IPFSDappBuildViewSet(IPFSDappViewMixin, BuildViewSet):
    pass


class IPFSDappEnvVarViewSet(IPFSDappViewMixin, EnvVarViewSet):
    pass


class IPFSDappLogViewSet(IPFSDappViewMixin, DappLogViewSet):
    pass


class IPFSDappGithubOptionsViewSet(IPFSDappViewMixin, GithubOptionsViewSet):
    pass
