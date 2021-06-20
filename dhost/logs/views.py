from rest_framework import viewsets

from dhost.dapps.views import DappViewMixin

from .models import APILog
from .serializers import APILogSerializer


class APILogViewSet(DappViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = APILog.objects.all()
    serializer_class = APILogSerializer
