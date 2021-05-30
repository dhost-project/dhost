from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from .dapps import views as dapps_views
from .github import views as github_views
from .ipfs import views as ipfs_views
from .logs import views as logs_views
from .users.api import views as users_views

router = routers.DefaultRouter()
router.register('bundles', dapps_views.DappBundleViewSet)
router.register('builds', dapps_views.DappBuildViewSet)
router.register('envvar', dapps_views.DappEnvironmentVariableViewSet)
router.register('github', github_views.GithubRepositoryViewSet)
router.register('ipfs', ipfs_views.IPFSDappViewSet)
router.register('ipfs_deploy', ipfs_views.IPFSDeploymentViewSet)
router.register('logs', logs_views.DashboardLogEntryViewSet)
router.register('users', users_views.UserViewSet)

urlpatterns = [
    path('oauth2/', include('dhost.oauth2.urls', namespace='oauth2_provider')),
    path('social/', include('social_django.urls', namespace='social')),
    path('u/', include('dhost.users.urls')),
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.ENABLE_DEBUG_TOOLBAR:  # pragma: no cover
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]

if settings.DEBUG:  # pragma: no cover
    from django.conf.urls.static import static
    from django.views import defaults as default_views

    urlpatterns += [
        path('api-auth/',
             include('rest_framework.urls', namespace='rest_framework')),
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
