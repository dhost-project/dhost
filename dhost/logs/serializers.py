from rest_framework import serializers

from .models import APILog


class APILogSerializer(serializers.ModelSerializer):

    class Meta:
        model = APILog
        fields = ['id', 'user', 'action_flag', 'change_message', 'action_time']
        read_only_fields = [
            'id',
            'user',
            'action_flag',
            'change_message',
            'action_time',
        ]
