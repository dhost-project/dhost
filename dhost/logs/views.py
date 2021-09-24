from rest_framework import viewsets

from dhost.dapps.views import DappViewMixin

from .models import DappLog
from .serializers import DappLogSerializer


class DappLogViewSet(DappViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = DappLog.objects.all()
    serializer_class = DappLogSerializer
