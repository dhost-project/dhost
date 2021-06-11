from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from dhost.builds.serializers import BuildOptionsSerializer
from dhost.github.serializers import BranchSerializer, RepositorySerializer
from dhost.logs.serializers import APILogSerializer

from .models import Dapp, DappGithubRepo, Deployment


class DeploymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deployment
        fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']
        read_only_fields = ['id', 'dapp', 'bundle', 'status', 'start', 'end']


class DappSerializer(BuildOptionsSerializer):

    deployments = DeploymentSerializer(many=True, read_only=True)
    logs = APILogSerializer(many=True, read_only=True)

    class Meta(BuildOptionsSerializer.Meta):
        model = Dapp
        fields = BuildOptionsSerializer.Meta.fields + [
            'slug', 'url', 'owner', 'status', 'deployments', 'logs',
            'created_at'
        ]
        read_only_fields = BuildOptionsSerializer.Meta.read_only_fields + [
            'url', 'owner', 'status', 'deployments', 'logs', 'created_at'
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


class DappGithubRepoSerializer(serializers.ModelSerializer):

    repo = RepositorySerializer(read_only=True)
    branch = BranchSerializer()

    class Meta:
        model = DappGithubRepo
        fields = ['repo', 'branch', 'auto_deploy', 'confirm_ci']
