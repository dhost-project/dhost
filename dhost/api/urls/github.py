from rest_framework import routers

from dhost.github.views import RepositoryViewSet, WebhookViewSet

router = routers.SimpleRouter()
router.register('repositories', RepositoryViewSet, basename='github_repos')
router.register('webhook', WebhookViewSet)
urlpatterns = router.urls
