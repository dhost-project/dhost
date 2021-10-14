from django.conf import settings
from django.urls import include, path

from dhost.api.views import (
    APIMetricsView,
    APIPingView,
    APIRootView,
    APITermsOfServiceView,
)

from .dapps import urlpatterns as dapps_urls
from .github import urlpatterns as github_urls
from .ipfs import urlpatterns as ipfs_urls
from .notifications import urlpatterns as notifications_urls
from .oauth2 import urlpatterns as oauth2_urls
from .users import urlpatterns as users_urls

app_name = "api"

urlpatterns = [
    path("", APIRootView.as_view()),
    path("metrics/", APIMetricsView.as_view(), name="metrics"),
    path("ping/", APIPingView.as_view(), name="ping"),
    path("tos/", APITermsOfServiceView.as_view(), name="tos"),
    path("dapps/", include(dapps_urls)),
    path("github/", include(github_urls)),
    path("ipfs/", include(ipfs_urls)),
    path("notifications/", include(notifications_urls)),
    path("oauth2/", include(oauth2_urls)),
    path("users/", include(users_urls)),
]

if settings.DEBUG:  # pragma: no cover
    from django.views.generic import TemplateView
    from rest_framework.permissions import AllowAny
    from rest_framework.schemas import get_schema_view

    from dhost import __version__
    from dhost.api.schema import SuperUserSchemaGenerator

    urlpatterns += [
        path(
            "openapi/",
            get_schema_view(
                title="DHost API",
                description=f"DHost REST API version {__version__}.",
                version=__version__,
                permission_classes=[AllowAny],
                generator_class=SuperUserSchemaGenerator,
            ),
            name="openapi-schema",
        ),
        path(
            "doc/",
            TemplateView.as_view(
                template_name="redoc.html",
                extra_context={"schema_url": "api:openapi-schema"},
            ),
            name="redoc",
        ),
    ]
