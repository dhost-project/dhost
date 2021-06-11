from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Branch, Repository, Webhook
from .permissions import HasGithubLinked
from .serializers import BranchSerializer, RepositorySerializer
from .webhook import PayloadHandler


class RepositoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    permission_classes = [HasGithubLinked]

    def get_queryset(self):
        """
        Overwriting `get_queryset` allow us to return 404 instead of return 403
        when the repo exist but the user doesn't have access (because it's not
        his for example).
        """
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)

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
        repos = Repository.objects.fetch_all(social)
        return Response(repos)


class GithubViewMixin:
    repo_model_class = Repository
    repo_reverse_name = 'repo'
    repo_url_slug = 'repo_slug'

    def get_repo(self):
        owner = self.request.user
        slug = self.kwargs[self.repo_url_slug]
        return get_object_or_404(self.repo_model_class, owner=owner, slug=slug)

    def get_queryset(self):
        repo = self.get_repo()
        filter_kwargs = {self.repo_reverse_name: repo}
        return super().get_queryset().filter(**filter_kwargs)


class BranchViewSet(GithubViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    @action(detail=False, methods=['get'])
    def fetch_branches(self, request):
        """Update branches from the Github API."""
        repo = self.get_repo()
        # branches = repo.fetch_branches()
        # TODO: to be removed
        branches = repo.branches.all()
        serializer = self.get_serializer(branches)
        return Response(serializer.data)


class WebhookViewSet(GithubViewMixin, viewsets.ViewSet):
    """View to receive webhooks from Github and handle them."""
    queryset = Webhook.objects.all()
    payload_handler_class = PayloadHandler

    def get_webhook(self):
        return self.get_object()

    def get_payload_handler(self, payload):
        return self.payload_handler_class(webhook=self.get_webhook(),
                                          payload=payload)

    @action(detail=True, methods=['post'])
    def payload(self, request, pk=None):
        payload = request.json()
        response = self.get_payload_handler(payload)
        return Response(response)
