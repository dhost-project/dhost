from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from dhost.dapps.views import DappViewMixin

from .models import GithubOptions, Repository, Webhook
from .permissions import HasGithubLinked
from .serializers import GithubOptionsSerializer, RepositorySerializer
from .webhook import PayloadHandler
from .github_api import GithubAPIError


class RepositoryViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer
    permission_classes = [HasGithubLinked]

    def get_queryset(self):
        # Return 404 instead of 403 when the repo exist but the user doesn't
        # have access.
        queryset = super().get_queryset()
        return queryset.filter(users=self.request.user)

    @action(detail=False, methods=['get'])
    def fetch_all(self, request):
        """Update every Github repos for user from the Github API."""
        try:
            Repository.objects.fetch_all(user=request.user)
        except GithubAPIError:
            content = {'detail': _('Error trying to fetch all repositories.')}
            return Response(
                content,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        repos = self.get_queryset()
        serializer = self.get_serializer(repos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def fetch(self, request, pk=None):
        """Update a single repo from Github API."""
        repo = self.get_object()
        try:
            repo.fetch_repo(user=request.user)
        except GithubAPIError:
            content = {'detail': _('Error trying to fetch repository.')}
            return Response(
                content,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        serializer = self.get_serializer(repo)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def fetch_branches(self, request, pk=None):
        """Update a single repo branches from the Github API."""
        repo = self.get_object()
        try:
            repo.fetch_branches(user=request.user)
        except GithubAPIError:
            content = {'detail': _('Error trying to fetch branches.')}
            return Response(
                content,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        serializer = self.get_serializer(repo)
        return Response(serializer.data)


class GithubOptionsViewSet(DappViewMixin, viewsets.ModelViewSet):
    queryset = GithubOptions.objects.all()
    serializer_class = GithubOptionsSerializer
    permission_classes = [HasGithubLinked]

    def perform_create(self, serializer):
        # Add `dapp` when creating the githuboptions
        serializer.save(dapp=self.get_dapp())


class WebhookViewSet(viewsets.ViewSet):
    """View to receive and handle webhooks from Github."""

    queryset = Webhook.objects.all()
    payload_handler_class = PayloadHandler
    permission_classes = [AllowAny]

    def get_webhook(self):
        return self.get_object()

    def get_payload_handler(self, payload):
        return self.payload_handler_class(
            webhook=self.get_webhook(),
            payload=payload,
        )

    @action(detail=True, methods=['post'])
    def payload(self, request, pk=None):
        """Receive a webhook payload from Github.

        This view will receive a webhook from Github and process it. It needs
        to send back a valid response or Github will disconnect it. We also
        need to send back a body containing a message, this will come from the
        payload handler class.

        Github docs:
            https://docs.github.com/en/github-ae@latest/developers/
        """
        payload = request.json()
        payload_handler = self.get_payload_handler(payload)
        response = payload_handler.handle()
        return Response(response)
