from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from dhost.builds.serializers import BuildOptionsSerializer
from dhost.users.api.serializers import UserSerializer

from .models import Dapp


class DappSerializer(BuildOptionsSerializer):

    owner = UserSerializer(read_only=True,
                           default=serializers.CurrentUserDefault())

    class Meta(BuildOptionsSerializer.Meta):
        model = Dapp
        fields = BuildOptionsSerializer.Meta.fields + [
            'slug', 'url', 'owner', 'status', 'created_at'
        ]
        read_only_fields = BuildOptionsSerializer.Meta.read_only_fields + [
            'url', 'owner', 'status', 'created_at'
        ]
        validators = [
            UniqueTogetherValidator(queryset=Dapp.objects.all(),
                                    fields=['owner', 'slug'])
        ]


class AbstractDeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
        read_only_fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
