from rest_framework import serializers

from dhost.builds.serializers import BuildOptionsSerializer

from .models import Dapp


class DappSerializer(BuildOptionsSerializer):

    class Meta(BuildOptionsSerializer.Meta):
        model = Dapp
        fields = BuildOptionsSerializer.Meta.fields + [
            'name', 'slug', 'url', 'owner', 'status', 'created_at'
        ]
        read_only_fields = BuildOptionsSerializer.Meta.read_only_fields + [
            'url', 'status', 'created_at'
        ]


class AbstractDeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
        read_only_fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
