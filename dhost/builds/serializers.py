from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Build, BuildOptions, Bundle, EnvironmentVariable


class BuildOptionsSerializer(serializers.ModelSerializer):
    builds = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='build-detail',
    )
    bundles = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='bundle-detail',
    )

    class Meta:
        model = BuildOptions
        fields = ['command', 'docker', 'builds', 'bundles']
        read_only_fields = []

    @action(detail=True, methods=['get'])
    def start_build(self, request, pk=None):
        build_options = self.get_object()
        is_success, _ = build_options.build()
        if is_success:
            return Response({'status': 'build successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BundleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bundle
        fields = ['id', 'options', 'created_at']
        read_only_fields = ['created_at']


class BuildSerializer(serializers.ModelSerializer):
    bundle = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='bundle-detail',
    )

    class Meta:
        model = Build
        fields = [
            'id', 'options', 'is_success', 'logs', 'bundle', 'start', 'end'
        ]
        read_only_fields = [
            'id', 'options', 'is_success', 'logs', 'start', 'end'
        ]


class EnvironmentVariableSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvironmentVariable
        fields = ['options', 'variable', 'value']
        read_only_fields = ['options']
