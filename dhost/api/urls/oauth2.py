from rest_framework import routers

from dhost.oauth2.views import (
    OAuth2AccessTokenViewSet,
    OAuth2ApplicationViewSet,
)

router = routers.SimpleRouter()
router.register(
    "applications", OAuth2ApplicationViewSet, basename="oauth2_application"
)
router.register("tokens", OAuth2AccessTokenViewSet, basename="oauth2_token")
urlpatterns = router.urls
