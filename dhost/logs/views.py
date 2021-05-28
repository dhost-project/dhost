from rest_framework import viewsets

from .models import DashboardLogEntry
from .serializers import DashboardLogEntrySerializer


class DashboardLogEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DashboardLogEntry.objects.all()
    serializer_class = DashboardLogEntrySerializer
