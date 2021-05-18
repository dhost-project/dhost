from rest_framework import serializers

from dhost.dapps.serializers import AbstractDeploymentSerializer, DappSerializer

from .models import IPFSDapp, IPFSDeployment


class IPFSDappSerializer(DappSerializer):
    deployments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='ipfsdeployment-detail',
    )

    class Meta(DappSerializer.Meta):
        model = IPFSDapp
        fields = DappSerializer.Meta.fields + ['deployments', 'hash']
        read_only_fields = DappSerializer.Meta.read_only_fields + [
            'deployments', 'hash'
        ]


class IPFSDeploymentSerializer(AbstractDeploymentSerializer):

    class Meta(AbstractDeploymentSerializer.Meta):
        model = IPFSDeployment
        fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
        read_only_fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
