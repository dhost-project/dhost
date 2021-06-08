from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import GithubRepo
from .permissions import HasGithubLinked
from .serializers import GithubRepoSerializer


class GithubRepoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = GithubRepo.objects.all()
    serializer_class = GithubRepoSerializer
    permission_classes = [HasGithubLinked]

    def get_queryset(self):
        """Overwriting `get_queryset` allow us to return 404 instead of return
        403 when the repo exist but the user doesn't have access (because it's
        not his for example).
        """
        queryset = super().get_queryset()
        social = self.request.user.social_auth.get(provider='github')
        queryset = queryset.filter(owner=social)
        return queryset

    @action(detail=True, methods=['get'])
    def fetch(self, request, pk=None):
        """Update a single repo from Github API."""
        repo = self.get_object()
        repo.fetch_repo()
        serializer = self.get_serializer(repo)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fetch_all(self, request):
        """Update every Github repos for user from the Github API."""
        social = request.user.social_auth.get(provider='github')
        repos = GithubRepo.objects.fetch_all(social)
        return Response(repos)
