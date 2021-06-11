from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested import routers

from .dapps import views as dapps_views
from .github import views as github_views
from .ipfs import views as ipfs_views
from .users.api import views as users_views

router = routers.DefaultRouter()
router.register('dapps', dapps_views.DappReadOnlyViewSet)

router.register('ipfs', ipfs_views.IPFSDappViewSet)
ipfs_router = routers.NestedSimpleRouter(router, 'ipfs', lookup='dapp')
ipfs_router.register('builds', ipfs_views.IPFSDappBuildViewSet)
ipfs_router.register('bundles', ipfs_views.IPFSDappBundleViewSet)
ipfs_router.register('deployments', ipfs_views.IPFSDeploymentViewSet)
ipfs_router.register('envvars', ipfs_views.IPFSDappEnvVarViewSet)
ipfs_router.register('logs', ipfs_views.IPFSDappAPILogViewSet)
ipfs_router.register('github', ipfs_views.IPFSDappGithubRepoViewSet)

router.register('github_webhook', github_views.WebhookViewSet)
router.register('users', users_views.UserViewSet)

api_urlpatterns = [
    path('', include(router.urls)),
    path('', include(ipfs_router.urls)),
]

urlpatterns = [
    path('oauth2/', include('dhost.oauth2.urls', namespace='oauth2_provider')),
    path('social/', include('social_django.urls', namespace='social')),
    path('u/', include('dhost.users.urls')),
    path('api/v1/', include(api_urlpatterns)),
    path('admin/', admin.site.urls),
]

if settings.ENABLE_DEBUG_TOOLBAR:  # pragma: no cover
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

if settings.DEBUG:  # pragma: no cover
    from django.conf.urls.static import static
    from django.views import defaults as default_views
    from django.views.generic import TemplateView
    from rest_framework.permissions import AllowAny
    from rest_framework.schemas import get_schema_view

    urlpatterns += [
        path('api-auth/',
             include('rest_framework.urls', namespace='rest_framework')),
        path('openapi',
             get_schema_view(
                 title="DHost",
                 description="API",
                 version="1.0.0",
                 url="http://localhost:8000/",
                 permission_classes=[AllowAny],
             ),
             name='openapi-schema'),
        path('redoc/',
             TemplateView.as_view(
                 template_name='redoc.html',
                 extra_context={'schema_url': 'openapi-schema'}),
             name='redoc'),
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
