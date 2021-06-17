from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from dhost.logs.serializers import APILogSerializer

from .models import Bundle, Dapp, Deployment


class BundleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bundle
        fields = ['id', 'created_at']


class DeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deployment
        fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
        read_only_fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']


class DappSerializer(serializers.ModelSerializer):

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    bundles = BundleSerializer(many=True, read_only=True)
    deployments = DeploymentSerializer(many=True, read_only=True)
    logs = APILogSerializer(many=True, read_only=True)

    class Meta:
        model = Dapp
        fields = [
            'id', 'slug', 'url', 'owner', 'status', 'created_at',
            'buildoptions', 'deployments', 'logs', 'bundles'
        ]
        read_only_fields = [
            'url', 'status', 'created_at', 'buildoptions', 'deployments', 'logs'
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
