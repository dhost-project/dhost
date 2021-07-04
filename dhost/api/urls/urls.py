from django.conf import settings
from django.urls import include, path
from rest_framework_nested import routers

from dhost.dapps import views as dapps_views
from dhost.github import views as github_views
from dhost.ipfs import views as ipfs_views
from dhost.users.api import views as users_views

router = routers.DefaultRouter()
router.register('dapps', dapps_views.DappReadOnlyViewSet)

router.register('ipfs', ipfs_views.IPFSDappViewSet)
ipfs_router = routers.NestedSimpleRouter(router, 'ipfs', lookup='dapp')
ipfs_router.register('buildoptions', ipfs_views.IPFSDappBuildOptionsViewSet)
ipfs_router.register('bundles', ipfs_views.IPFSDappBundleViewSet)
ipfs_router.register('deployments', ipfs_views.IPFSDeploymentViewSet)
ipfs_router.register('logs', ipfs_views.IPFSDappAPILogViewSet)
ipfs_router.register('githuboptions', ipfs_views.IPFSDappGithubOptionsViewSet)

ipfs_build_router = routers.NestedSimpleRouter(ipfs_router,
                                               'buildoptions',
                                               lookup='buildoptions')
ipfs_build_router.register('builds', ipfs_views.IPFSDappBuildViewSet)
ipfs_build_router.register('envvars', ipfs_views.IPFSDappEnvVarViewSet)

router.register('github/repositories', github_views.RepositoryViewSet)
router.register('github/webhook', github_views.WebhookViewSet)

router.register('users', users_views.UserViewSet)

api_v1_urlpatterns = [
    path('', include(router.urls)),
    path('', include(ipfs_router.urls)),
    path('', include(ipfs_build_router.urls)),
]

urlpatterns = [
    path('v1/', include(api_v1_urlpatterns)),
]

if settings.SETTINGS_MODULE == 'dhost.settings.development':  # pragma: no cover
    from django.views.generic import TemplateView
    from rest_framework.permissions import AllowAny
    from rest_framework.schemas import get_schema_view

    urlpatterns += [
        path(
            'api-auth/',
            include('rest_framework.urls', namespace='rest_framework'),
        ),
        path(
            'openapi',
            get_schema_view(
                title="DHost",
                description="API",
                version="1.1.0",
                url="",
                permission_classes=[AllowAny],
            ),
            name='openapi-schema',
        ),
        path(
            'redoc/',
            TemplateView.as_view(
                template_name='redoc.html',
                extra_context={'schema_url': 'openapi-schema'},
            ),
            name='redoc',
        ),
    ]
