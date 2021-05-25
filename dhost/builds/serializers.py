from rest_framework import serializers

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
        fields = ['id', 'command', 'docker', 'builds', 'bundles']
        read_only_fields = []


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
        # read_only_fields = ['options']
