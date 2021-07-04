from rest_framework import routers

from dhost.users.api.views import UserViewSet

router = routers.SimpleRouter()
router.register('', UserViewSet)
urlpatterns = router.urls
