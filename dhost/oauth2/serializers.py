from oauth2_provider.models import AccessToken
from rest_framework import serializers

from dhost.oauth2.models import OAuth2Application


class OAuth2ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = OAuth2Application
        fields = ('id', 'user', 'name', 'description', 'logo', 'client_id',
                  'client_secret', 'client_type', 'authorization_grant_type',
                  'skip_authorization', 'created', 'updated')
        read_only_fields = ('client_id', 'client_secret')


class OAuth2AccessTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessToken
        fields = ('id', 'expires', 'scope', 'created', 'updated', 'application')
