from oauth2_provider.models import AccessToken
from rest_framework import viewsets

from dhost.oauth2.models import OAuth2Application
from dhost.oauth2.serializers import (
    OAuth2AccessTokenSerializer,
    OAuth2ApplicationSerializer,
)


class OAuth2ApplicationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OAuth2Application.objects.all()
    serializer_class = OAuth2ApplicationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class OAuth2AccessTokenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AccessToken.objects.all()
    serializer_class = OAuth2AccessTokenSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
