from django.conf import settings
from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from dhost.utils import get_version


class APIRootView(APIView):
    permission_classes = (AllowAny,)
    name = "API Root"
    description = "DHost REST API"

    def get(self, request, format=None):
        """REST API root."""
        response = {
            "ping": reverse_lazy(
                "api:ping",
                request=request,
            ),
            "dapps": reverse_lazy(
                "api:dapp-list",
                request=request,
            ),
            "github_repos": reverse_lazy(
                "api:github_repo-list",
                request=request,
            ),
            "ipfs_dapps": reverse_lazy(
                "api:ipfs_dapp-list",
                request=request,
            ),
            "notifications": reverse_lazy(
                "api:notification-list",
                request=request,
            ),
            "applications": reverse_lazy(
                "api:oauth2_application-list",
                request=request,
            ),
            "tokens": reverse_lazy(
                "api:oauth2_token-list",
                request=request,
            ),
            "me": reverse_lazy(
                "api:user-me",
                request=request,
            ),
        }

        if settings.SETTINGS_MODULE == "dhost.settings.development":
            response.update(
                {
                    "doc": reverse_lazy(
                        "api:redoc",
                        request=request,
                    ),
                    "schema": reverse_lazy(
                        "api:openapi-schema",
                        request=request,
                    ),
                }
            )

        return Response(response)


class APIPingView(APIView):
    permission_classes = (AllowAny,)
    name = "Ping"

    def get(self, request, format=None):
        response = {"version": get_version()}
        return Response(response)


class APITermsOfServiceView(TemplateView):
    permission_classes = (AllowAny,)
    name = "TermsOfService"
    template_name = "api_tos.html"
