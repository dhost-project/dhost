from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.api.viewsets import DestroyListRetrieveViewSet

from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(DestroyListRetrieveViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    @action(detail=True, methods=['get'])
    def read(self, request, pk=None):
        """Mark notification has read."""
        notification = self.get_object()
        notification.read_by_user()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def unread(self, request, pk=None):
        """Mark notification has un-read."""
        notification = self.get_object()
        notification.unread_by_user()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)
