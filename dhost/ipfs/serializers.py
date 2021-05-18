from dhost.dapps.serializers import AbstractDeploymentSerializer, DappSerializer

from .models import IPFSDapp, IPFSDeployment


class IPFSDappSerializer(DappSerializer):

    class Meta(DappSerializer.Meta):
        model = IPFSDapp
        fields = DappSerializer.Meta.fields + ['hash']
        read_only_fields = DappSerializer.Meta.read_only_fields + ['hash']


class IPFSDeploymentSerializer(AbstractDeploymentSerializer):

    class Meta(AbstractDeploymentSerializer.Meta):
        model = IPFSDeployment
        fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
        read_only_fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
