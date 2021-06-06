from dhost.dapps.serializers import AbstractDeploymentSerializer, DappSerializer

from .models import IPFSDapp, IPFSDeployment


class IPFSDeploymentSerializer(AbstractDeploymentSerializer):

    class Meta(AbstractDeploymentSerializer.Meta):
        model = IPFSDeployment
        fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
        read_only_fields = AbstractDeploymentSerializer.Meta.fields + ['hash']


class IPFSDappSerializer(DappSerializer):
    deployments = IPFSDeploymentSerializer(
        many=True,
        read_only=True,
    )

    class Meta(DappSerializer.Meta):
        model = IPFSDapp
        fields = DappSerializer.Meta.fields + [
            'ipfs_gateway', 'deployments', 'hash'
        ]
        read_only_fields = DappSerializer.Meta.read_only_fields + [
            'deployments', 'hash'
        ]
