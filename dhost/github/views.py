from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import GithubRepository
from .github import GithubAPI, GithubNotLinkedError


class GithubRepositoryViewSet(viewsets.GenericViewSet):
    queryset = GithubRepository.objects.all()

    @action(detail=False, methods=['get'])
    def repositories(self, request, pk=None):
        try:
            github = GithubAPI(user=request.user)
        except GithubNotLinkedError as e:
            data = {'details': str(e)}
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        else:
            data = github.get_repos()
            return Response(data)
