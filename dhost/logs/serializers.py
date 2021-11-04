from rest_framework import serializers

from .models import DappLog


class DappLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DappLog
        fields = ["id", "user", "action_flag", "change_message", "action_time"]
        read_only_fields = [
            "id",
            "user",
            "action_flag",
            "change_message",
            "action_time",
        ]
