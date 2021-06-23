from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Build, BuildOptions, EnvVar


class BuildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Build
        fields = ['id', 'is_success', 'logs', 'bundle', 'start', 'end']


class EnvVarSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvVar
        fields = ['variable', 'value']
        # read_only_fields = ['options']
        validators = [
            UniqueTogetherValidator(
                queryset=EnvVar.objects.all(),
                fields=['buildoptions', 'variable'],
            )
        ]


class BuildOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuildOptions
        fields = ['command', 'docker']
