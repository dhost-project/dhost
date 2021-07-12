from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dhost.api.urls')),
    path('oauth2/', include('dhost.oauth2.urls', namespace='oauth2_provider')),
    path('social/', include('social_django.urls', namespace='social')),
    path('u/', include('dhost.users.urls')),
]

if settings.SETTINGS_MODULE == 'dhost.settings.development':  # pragma: no cover
    from django.conf.urls.static import static
    from django.views import defaults as default_views

    urlpatterns += [
        path(
            'api-auth/',
            include('rest_framework.urls', namespace='rest_framework'),
        ),
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
