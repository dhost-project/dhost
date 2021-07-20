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

    @action(detail=False, methods=["get"])
    def count(self, request):
        """Total count of notifications."""
        data = {"count": self.get_queryset().count()}
        return Response(data)

    @action(detail=False, methods=["get"])
    def unread_count(self, request):
        """Count of unread notifications."""
        data = {"count": self.get_queryset().unread().count()}
        return Response(data)

    @action(detail=True, methods=["get"])
    def read(self, request, pk=None):
        """Mark notification has read."""
        notification = self.get_object()
        notification.mark_as_read()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def unread(self, request, pk=None):
        """Mark notification has unread."""
        notification = self.get_object()
        notification.mark_as_unread()
        serializer = self.get_serializer(notification)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def mark_all_as_read(self, request):
        """Mark all notifications has read."""
        data = {"count": self.get_queryset().mark_all_as_read()}
        return Response(data)

    @action(detail=False, methods=["get"])
    def mark_all_as_unread(self, request):
        """Mark all notifications has unread."""
        data = {"count": self.get_queryset().mark_all_as_unread()}
        return Response(data)
