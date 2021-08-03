from rest_framework import serializers

from .models import Build, BuildOptions, EnvVar

# from rest_framework.validators import UniqueTogetherValidator


class BuildOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildOptions
        fields = ["command", "docker"]


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = ["id", "is_success", "logs", "bundle", "start", "end"]


class EnvVarSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvVar
        fields = ["id", "variable", "value", "sensitive"]
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=EnvVar.objects.all(),
        #         fields=["buildoptions", "variable"],
        #     )
        # ]

    def to_representation(self, obj):
        """Hide the value if it's a sensitive variable."""
        rep = super().to_representation(obj)
        if obj.sensitive:
            rep["value"] = None
        return rep
