from django.conf import settings
from django.urls import include, path

from .dapps import urlpatterns as dapps_urls
from .github import urlpatterns as github_urls
from .ipfs import urlpatterns as ipfs_urls
from .users import urlpatterns as users_urls

api_v1_urlpatterns = [
    path('dapps/', include(dapps_urls)),
    path('github/', include(github_urls)),
    path('ipfs/', include(ipfs_urls)),
    path('users/', include(users_urls)),
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
