from django.urls import include, path

from .views import DappBundleViewSet, DappViewSet

dapp_list = DappViewSet.as_view({'get': 'list'})
dapp_details = DappViewSet.as_view({'get': 'retrieve'})
bundle_list = DappBundleViewSet.as_view({'get': 'list'})
bundle_details = DappBundleViewSet.as_view({'get': 'retrieve'})

dapp_urlpatterns = [
    path('', dapp_details),
    path('bundles/', bundle_list),
    path('bundles/<uuid:bundle__id>/', bundle_details),
]

urlpatterns = [
    path('<str:username>/', dapp_list),
    path('<str:username>/<str:dapp__slug>/', include(dapp_urlpatterns)),
]
