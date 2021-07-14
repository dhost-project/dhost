from rest_framework import routers

from dhost.notifications.views import NotificationViewSet

router = routers.SimpleRouter()
router.register('', NotificationViewSet, basename='notification')
urlpatterns = router.urls
