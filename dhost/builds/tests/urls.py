from rest_framework import routers

from .. import views

router = routers.SimpleRouter()
router.register('options', views.BuildOptionsViewSet)
router.register('bundles', views.BundleViewSet)
router.register('builds', views.BuildsViewSet)
router.register('envvar', views.EnvironmentVariableViewSet)

urlpatterns = router.urls
