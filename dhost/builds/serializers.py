from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Build, EnvVar


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
