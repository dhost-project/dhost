from rest_framework import serializers

from .models import DashboardLogEntry


class DashboardLogEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = DashboardLogEntry
        fields = ['id', 'user', 'action_flag', 'change_message', 'action_time']
        read_only_fields = [
            'id', 'user', 'action_flag', 'change_message', 'action_time'
        ]
