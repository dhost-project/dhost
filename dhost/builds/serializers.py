from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Build, BuildOptions, EnvVar


class BuildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Build
        fields = [
            'id', 'options', 'is_success', 'logs', 'bundle', 'start', 'end'
        ]


class EnvVarSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvVar
        fields = ['options', 'variable', 'value']
        # read_only_fields = ['options']
        validators = [
            UniqueTogetherValidator(queryset=EnvVar.objects.all(),
                                    fields=['options', 'variable'])
        ]


class BuildOptionsSerializer(serializers.ModelSerializer):
    builds = BuildSerializer(many=True, read_only=True)
    envvars = EnvVarSerializer(many=True, read_only=True)

    class Meta:
        model = BuildOptions
        fields = ['command', 'docker', 'builds', 'envvars']
        read_only_fields = ['builds', 'envvars']
