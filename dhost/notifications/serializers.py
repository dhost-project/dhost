from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ['id', 'subject', 'content', 'read', 'url', 'time']
        read_only_fields = ['id', 'subject', 'content', 'read', 'url', 'time']
