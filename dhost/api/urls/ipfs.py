from django.urls import include, path
from rest_framework_nested import routers

from dhost.ipfs.views import (IPFSDappAPILogViewSet,
                              IPFSDappBuildOptionsViewSet, IPFSDappBuildViewSet,
                              IPFSDappBundleViewSet, IPFSDappEnvVarViewSet,
                              IPFSDappGithubOptionsViewSet, IPFSDappViewSet,
                              IPFSDeploymentViewSet)

router = routers.SimpleRouter()

router.register('', IPFSDappViewSet)

ipfs_router = routers.NestedSimpleRouter(router, '', lookup='dapp')
ipfs_router.register('buildoptions', IPFSDappBuildOptionsViewSet)
ipfs_router.register('bundles', IPFSDappBundleViewSet)
ipfs_router.register('deployments', IPFSDeploymentViewSet)
ipfs_router.register('logs', IPFSDappAPILogViewSet)
ipfs_router.register('githuboptions', IPFSDappGithubOptionsViewSet)

ipfs_build_router = routers.NestedSimpleRouter(ipfs_router,
                                               'buildoptions',
                                               lookup='buildoptions')
ipfs_build_router.register('builds', IPFSDappBuildViewSet)
ipfs_build_router.register('envvars', IPFSDappEnvVarViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(ipfs_router.urls)),
    path('', include(ipfs_build_router.urls)),
]
