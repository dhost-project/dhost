from rest_framework import serializers

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

    class Meta:
        model = Dapp
        fields = ['slug', 'url', 'owner', 'status', 'created_at']
        read_only_fields = ['url', 'status', 'created_at']


class DappReadOnlySerializer(serializers.ModelSerializer):

    dapp_type = serializers.CharField(source='get_dapp_type', read_only=True)

    class Meta:
        model = Dapp
        fields = ['slug', 'dapp_type', 'url', 'owner', 'status']
