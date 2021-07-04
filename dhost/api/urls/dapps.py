from rest_framework import routers

from dhost.dapps.views import DappReadOnlyViewSet

router = routers.SimpleRouter()
router.register('', DappReadOnlyViewSet)
urlpatterns = router.urls
