from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Dapp

from .github import DjangoGithubAPI
from .managers import (BranchManager, RepositoryManager, WebhookManager,
                       serialize_branch,
                       serialize_repository, serialize_webhook)
from .utils import get_user_github_account


class Repository(models.Model):
    """
    Model representing a Github repository, the instance is created and updated
    from the response of the Github API.
    """
    id = models.IntegerField(
        _('Github ID'),
        primary_key=True,
        unique=True,
        help_text=_('Github repository unique ID.')
    )
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    github_owner = models.CharField(max_length=256)
    github_repo = models.CharField(max_length=256)
    # full raw output from the Github API
    extra_data = models.JSONField(default=dict, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, help_text=_('Added at.'))
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('Last updated from the Github API.'),
    )
    objects = RepositoryManager()

    class Meta:
        verbose_name = _('Github repository')
        verbose_name_plural = _('Github repositories')

    def fetch_repo(self, user):
        """Fetch repo from the Github API and update it."""
        github_account = get_user_github_account(user)
        g = DjangoGithubAPI(github_account=github_account)
        repo_json = g.get_repo(owner=self.github_owner, repo=self.github_repo)
        self.update_from_json(repo_json)

    def update_from_json(self, repo_json, user=None):
        data = serialize_repository(repo_json)
        self.github_owner = data['github_owner']
        self.github_repo = data['github_repo']
        self.extra_data = data['extra_data']
        if user not in self.users.all():
            self.users.add(user)
        self.updated_at = timezone.now()
        self.save()

    def download(self, path):
        """Download repo from Github API."""
        g = DjangoGithubAPI(social=self.owner)
        tar_name = g.download_repo(self.github_full_name, path)
        return tar_name

    def fetch_branches(self, user):
        Branch.objects.fetch_repo_branches(self, user)

    def create_webhook(self, **kwargs):
        """Create a webhook object linked to this Github repo."""
        kwargs.update({'repo': self.id})
        Webhook.objects.create_github_webhook(**kwargs)


class Branch(models.Model):
    repo = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name='branches',
        related_query_name='branches',
    )
    name = models.CharField(max_length=255)
    extra_data = models.JSONField(default=dict, blank=True)
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('Last updated from the Github API.'),
    )
    objects = BranchManager()

    class Meta:
        verbose_name = _('Branch')
        verbose_name_plural = _("Branches")

    def update_from_json(self, branch_json):
        data = serialize_branch(branch_json)
        self.extra_data = data['extra_data']
        self.updated_at = timezone.now()
        self.save()


class Webhook(models.Model):
    id = models.IntegerField(
        _('Github ID'),
        primary_key=True,
        unique=True,
        help_text=_('Github webhook unique ID.')
    )
    repo = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
        related_name='webhooks',
        related_query_name='webhooks',
    )
    name = models.CharField(max_length=255, default='web')
    active = models.BooleanField(default=True)
    extra_data = models.JSONField(default=dict, blank=True)
    added_at = models.DateTimeField(auto_now_add=True, help_text=_('Added at.'))
    updated_at = models.DateTimeField(
        default=timezone.now,
        help_text=_('Last updated from the Github API.'),
    )
    last_called_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text=_('Last called by Github.'),
    )
    objects = WebhookManager()

    class Meta:
        verbose_name = _('Github webhook')
        verbose_name_plural = _('Github webhooks')

    def delete(self, *args, **kwargs):
        # TODO: signal Github to remove webhooks
        return super().delete(*args, **kwargs)

    def update_from_json(self, branch_json):
        data = serialize_webhook(branch_json)
        self.name = data['name']
        self.active = data['active']
        self.extra_data = data['extra_data']
        self.updated_at = timezone.now()
        self.save()

    def activate(self):
        pass

    def deactivate(self):
        """
        Deactivate only if there is no DappGithubRepo linked to it that have
        `auto_deploy` turned on.
        """
        pass


class GithubOptions(models.Model):
    """
    Represent the link between a Dapp and a Github repository, it also add some
    options related to the deployment `auto_deploy` specifies if the Dapp
    should be re-deployed when a webhook linked to that repo is called.
    It also contains the branch to be used when downloading the repo.
    """
    dapp = models.OneToOneField(
        Dapp,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    repo = models.ForeignKey(
        Repository,
        on_delete=models.CASCADE,
    )
    branch = models.ForeignKey(Branch, null=True, on_delete=models.SET_NULL)
    auto_deploy = models.BooleanField(
        default=False,
        help_text=_('Automatically deploy the dapp when a push is made on the '
                    'selected branch.'),
    )
    # If auto_deploy is True and confirm_ci is True it will auto deploy but
    # only if the CI are successful
    confirm_ci = models.BooleanField(
        default=False,
        help_text=_(
            'Wait for CI to pass before automatically deploying the dapp.'
        ),
    )

    class Meta:
        verbose_name = _('Dapp Github options')
        verbose_name_plural = _('Dapps Github options')
