from dhost.dapps.serializers import (AbstractDappSerializer,
                                     AbstractDeploymentSerializer)

from .models import IPFSDapp, IPFSDeployment


class IPFSDappSerializer(AbstractDappSerializer):

    class Meta(AbstractDappSerializer.Meta):
        model = IPFSDapp
        fields = AbstractDappSerializer.Meta.fields + ['hash']
        read_only_fields = AbstractDappSerializer.Meta.read_only_fields + [
            'hash'
        ]


class IPFSDeploymentSerializer(AbstractDeploymentSerializer):

    class Meta(AbstractDeploymentSerializer.Meta):
        model = IPFSDeployment
        fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
        read_only_fields = AbstractDeploymentSerializer.Meta.fields + ['hash']
