from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "gravatar_hash"]
        read_only_fields = ["id", "gravatar_hash"]
