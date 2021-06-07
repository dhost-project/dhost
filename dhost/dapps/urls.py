from django.urls import path

from .views import (DappBuildViewSet, DappBundleViewSet, DappViewSet,
                    EnvironmentVariableViewSet)

dapp_list = DappViewSet.as_view({'get': 'list', 'post': 'create'})
dapp_details = DappViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
dapp_build = DappViewSet.as_view({'get': 'build'})
dapp_deploy = DappViewSet.as_view({'get': 'deploy'})
envvar_list = EnvironmentVariableViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
envvar_details = EnvironmentVariableViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
bundle_list = DappBundleViewSet.as_view({'get': 'list'})
bundle_details = DappBundleViewSet.as_view({'get': 'retrieve'})
build_list = DappBuildViewSet.as_view({'get': 'list'})
build_details = DappBuildViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('', dapp_list),
    path('<slug:dapp__slug>/', dapp_details),
    path('<slug:dapp__slug>/build/', dapp_build),
    path('<slug:dapp__slug>/deploy/', dapp_deploy),
    path('<slug:dapp__slug>/envvars/', envvar_list),
    path('<slug:dapp__slug>/envvars/<uuid:pk>/', envvar_details),
    path('<slug:dapp__slug>/bundles/', bundle_list),
    path('<slug:dapp__slug>/bundles/<uuid:pk>/', bundle_details),
    path('<slug:dapp__slug>/builds/', build_list),
    path('<slug:dapp__slug>/builds/<uuid:pk>/', build_details),
    path('<slug:dapp__slug>/deployments/', build_list),
    path('<slug:dapp__slug>/deployments/<uuid:pk>/', build_details),
]
