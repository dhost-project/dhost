from dhost.dapps.serializers import DappSerializer, DeploymentSerializer

from .models import IPFSDapp, IPFSDeployment


class IPFSDeploymentSerializer(DeploymentSerializer):

    class Meta(DeploymentSerializer.Meta):
        model = IPFSDeployment
        fields = DeploymentSerializer.Meta.fields + ['hash']
        read_only_fields = DeploymentSerializer.Meta.fields + ['hash']


class IPFSDappSerializer(DappSerializer):
    deployments = IPFSDeploymentSerializer(many=True, read_only=True)

    class Meta(DappSerializer.Meta):
        model = IPFSDapp
        fields = DappSerializer.Meta.fields + ['ipfs_gateway', 'hash']
        read_only_fields = DappSerializer.Meta.read_only_fields + ['hash']
