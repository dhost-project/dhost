from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = [
            'id', 'subject', 'content', 'read', 'level', 'url', 'timestamp'
        ]
        read_only_fields = [
            'id', 'subject', 'content', 'level', 'url', 'timestamp'
        ]
