from django.conf import settings
from django.db import models


class AbstractGit(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    repo_name = models.CharField(max_length=1024)
    branch = models.CharField(max_length=1024, default='master')
    auto_deploy = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def download_source(self):
        pass


class CommitMixin(models.Model):
    git = None
    commit_hash = models.CharField(max_length=42)

    class Meta:
        abstract = True

    def __str__(self):
        return self.commit_hash


class Github(AbstractGit):
    repo_url = models.URLField()

    class Meta(AbstractGit.Meta):
        pass


class GithubCommit(CommitMixin):
    git = models.ForeignKey(Github, on_delete=models.CASCADE)

    class Meta(CommitMixin.Meta):
        pass
