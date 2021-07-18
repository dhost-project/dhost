from rest_framework import routers

from dhost.github.views import RepositoryViewSet, WebhookViewSet

router = routers.SimpleRouter()
router.register('repositories', RepositoryViewSet, basename='github_repo')
router.register('webhook', WebhookViewSet, basename='github_webhook')
urlpatterns = router.urls
