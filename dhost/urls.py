from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("dhost.api.urls")),
    path("oauth2/", include("dhost.oauth2.urls", namespace="oauth2_provider")),
    path("social/", include("social_django.urls", namespace="social")),
    path("u/", include("dhost.users.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt",
            content_type="text/plain",
        ),
    ),
]

admin.site.site_header = "DHost"
admin.site.site_title = "dhost"

if settings.SETTINGS_MODULE == "dhost.settings.development":  # pragma: no cover
    from django.conf.urls.static import static

    urlpatterns.append(
        path(
            "api-auth/",
            include("rest_framework.urls", namespace="rest_framework"),
        )
    )

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# added last to redirect any URL not previously handled by Django to the react
# dashboard wich will route the URL itself in the browser
urlpatterns += [re_path(".*", include("dhost.frontend.urls"))]
