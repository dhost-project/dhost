from rest_framework import routers

from dhost.dapps.views import DappReadOnlyViewSet

router = routers.SimpleRouter()
router.register("", DappReadOnlyViewSet, basename="dapp")
urlpatterns = router.urls
