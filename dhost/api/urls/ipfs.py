from django.urls import include, path
from rest_framework import routers

from dhost.ipfs.views import (IPFSDappAPILogViewSet,
                              IPFSDappBuildOptionsViewSet, IPFSDappBuildViewSet,
                              IPFSDappBundleViewSet, IPFSDappEnvVarViewSet,
                              IPFSDappGithubOptionsViewSet, IPFSDappViewSet,
                              IPFSDeploymentViewSet)

router = routers.SimpleRouter()
router.register('', IPFSDappViewSet, basename='ipfs_dapp')

ipfs_router = routers.SimpleRouter()
ipfs_router.register('bundles', IPFSDappBundleViewSet)
ipfs_router.register('deployments', IPFSDeploymentViewSet)
ipfs_router.register('githuboptions', IPFSDappGithubOptionsViewSet)
ipfs_router.register('logs', IPFSDappAPILogViewSet)

ipfs_build_router = routers.SimpleRouter()
ipfs_build_router.register('builds', IPFSDappBuildViewSet)
ipfs_build_router.register('envvars', IPFSDappEnvVarViewSet)

nested_urls = [
    path('', include(ipfs_router.urls)),
    path(
        'buildoptions/',
        IPFSDappBuildOptionsViewSet.as_view({
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        })),
    path('buildoptions/', include(ipfs_build_router.urls)),
]

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:dapp_slug>/', include(nested_urls)),
]
