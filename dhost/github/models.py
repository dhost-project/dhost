from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from social_django.models import UserSocialAuth

from .github import DjangoGithubAPI


class AbstractGit(models.Model):
    owner = models.ForeignKey(
        UserSocialAuth,
        on_delete=models.CASCADE,
    )
    # max repo name length on Github is 100
    name = models.CharField(max_length=256)
    branch = models.CharField(max_length=256, default='main')
    size = models.SmallIntegerField(null=True, blank=True)
    auto_deploy = models.BooleanField(default=False)
    updated = models.DateTimeField(
        null=True,
        blank=True,
        editable=False,
        help_text='Last updated from external source.',
    )
    created = models.DateTimeField(auto_now_add=True, help_text='Created at.')
    modified = models.DateTimeField(
        auto_now=True,
        help_text='Last modified by user or external source.',
    )

    class Meta:
        abstract = True

    def download_repo(self):
        raise NotImplementedError


class GithubRepoManager(models.Manager):

    def fetch_all(self, github_social):
        # TODO remove repos that are not present in the response because they
        # are either deleted or unaccessible
        g = DjangoGithubAPI(github_social=github_social)
        repos = g.get_repos()
        for repo in repos:
            self.update_or_create_from_json(github_social, repo)
        return repos

    def create_from_json(self, owner, repo_json):
        """Create a GithubRepository from a Github API response."""
        github_id = repo_json['id']
        github_owner = repo_json['owner']['login']
        github_repo = repo_json['name']
        size = repo_json['size']
        github_extra_data = repo_json
        return self.create(owner=owner,
                           name=github_repo,
                           size=size,
                           github_id=github_id,
                           github_owner=github_owner,
                           github_repo=github_repo,
                           github_extra_data=github_extra_data)

    def update_or_create_from_json(self, owner, repo_json):
        """Like get_or_create but from Github API response and update instead
        of just getting the object when it exist.
        """
        github_id = repo_json['id']
        try:
            github_repo = self.get(github_id=github_id, owner=owner)
            github_repo.update_from_json(repo_json)
            return github_repo
        except GithubRepo.DoesNotExist:
            return self.create_from_json(owner, repo_json)


class GithubRepo(AbstractGit):
    github_id = models.IntegerField()
    github_owner = models.CharField(max_length=256)
    github_repo = models.CharField(max_length=256)
    # full raw output from the Github API
    github_extra_data = models.JSONField(null=True, blank=True)
    objects = GithubRepoManager()

    class Meta(AbstractGit.Meta):
        verbose_name = _('Github repository')
        verbose_name_plural = _('Github repositories')

    def fetch_repo(self):
        """Fetch repo from the Github API and update it."""
        g = DjangoGithubAPI(github_social=self.owner)
        repo_json = g.get_repo(owner=self.github_owner, repo=self.github_repo)
        self.update_from_json(repo_json)

    def update_from_json(self, repo_json):
        self.size = repo_json['size']
        self.github_owner = repo_json['owner']['login']
        self.github_repo = repo_json['name']
        self.github_extra_data = repo_json
        self.updated = timezone.now()
        self.save()

    def download_repo(self, path):
        """Download repo from Github API."""
        g = DjangoGithubAPI(social=self.owner)
        tar_name = g.download_repo(self.github_full_name, path)
        # TODO decompress
        print(tar_name)
        source_path = None
        return source_path
