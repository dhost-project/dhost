from rest_framework import viewsets

from .models import APILog
from .serializers import APILogSerializer


class APILogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = APILog.objects.all()
    serializer_class = APILogSerializer
