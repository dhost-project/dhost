from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from dhost.builds.serializers import (BuildSerializer, BundleSerializer,
                                      EnvVarSerializer)
from dhost.logs.serializers import APILogSerializer

from .models import Dapp, Deployment


class DeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deployment
        fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
        read_only_fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']


class DappSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    builds = BuildSerializer(many=True, read_only=True)
    bundles = BundleSerializer(many=True, read_only=True)
    envvars = EnvVarSerializer(many=True, read_only=True)
    deployments = DeploymentSerializer(many=True, read_only=True)
    logs = APILogSerializer(many=True, read_only=True)

    class Meta:
        model = Dapp
        fields = [
            'id', 'slug', 'url', 'owner', 'status', 'deployments', 'logs',
            'created_at', 'command', 'docker', 'builds', 'bundles', 'envvars'
        ]
        read_only_fields = [
            'url', 'status', 'deployments', 'logs', 'created_at'
        ]
        validators = [
            UniqueTogetherValidator(queryset=Dapp.objects.all(),
                                    fields=['owner', 'slug'])
        ]


class DappReadOnlySerializer(serializers.ModelSerializer):
    dapp_type = serializers.CharField(source='get_dapp_type', read_only=True)

    class Meta:
        model = Dapp
        fields = ['id', 'dapp_type', 'slug', 'url', 'owner', 'status']
