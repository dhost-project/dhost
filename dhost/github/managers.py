from django.apps import apps
from django.db import models

from .github import DjangoGithubAPI


def serialize_github_repo(repo_json):
    """Serialize from the Github API to a dict."""
    return {
        'github_id': repo_json['id'],
        'github_owner': repo_json['owner']['login'],
        'github_repo': repo_json['name'],
        'extra_data': repo_json,
    }


def serialize_github_branch(branch_json):
    return {
        'name': branch_json['name'],
        'extra_data': branch_json,
    }


def serialize_github_webhook(webhook_json):
    return {
        'github_id': webhook_json['id'],
        'name': webhook_json['name'],
        'active': webhook_json['active'],
        'extra_data': webhook_json,
    }


class RepositoryManager(models.Manager):

    def fetch_all(self, github_social):
        # TODO remove repos that are not present in the response because they
        # are either deleted or unavailable
        g = DjangoGithubAPI(github_social=github_social)
        repos = g.list_repos()
        for repo in repos:
            self.update_or_create_from_json(github_social, repo)
        return repos

    def create_from_json(self, owner, repo_json):
        """Create a Repositorysitory from a Github API response."""
        data = self.serialize(repo_json)
        data.update({'owner': owner})
        return self.create(**data)

    def update_or_create_from_json(self, owner, repo_json):
        """
        Like get_or_create but from Github API response and update instead of
        just getting the object when it exist.
        """
        Repository = apps.get_model('github.Repository')
        github_id = repo_json['id']
        try:
            github_repo = self.get(github_id=github_id, owner=owner)
            github_repo.update_from_json(repo_json)
            return github_repo
        except Repository.DoesNotExist:
            return self.create_from_json(owner, repo_json)

    def serialize(self, repo_json):
        return serialize_github_repo(repo_json)


class BranchManager(models.Manager):

    def fetch_repo_branches(self, repo, github_social):
        # TODO remove branches that are not present in the response because
        # they are either deleted or inavailable
        g = DjangoGithubAPI(github_social=github_social)
        branches = g.list_branches(repo=repo)
        for branch in branches:
            self.update_or_create_from_json(repo, branch)
        return branches

    def create_from_json(self, repo, branch_json):
        data = self.serialize(branch_json)
        data.update({'repo': repo})
        return self.create(**data)

    def update_or_create_from_json(self, repo, branch_json):
        Branch = apps.get_model('github.Branch')
        name = branch_json['name']
        try:
            branch = self.get(name=name, repo=repo)
            branch.update_from_json(branch_json)
            return branch
        except Branch.DoesNotExist:
            return self.create_from_json(repo, branch_json)

    def serialize(self, branch_json):
        return serialize_github_branch(branch_json)


class WebhookManager(models.Manager):

    def create_github_webhook(self, repo, owner, name='web'):
        g = DjangoGithubAPI()
        webhook_json = g.create_webhook(owner=owner, repo=repo, name=name)
        return self.create_from_json(repo=repo, webhook_json=webhook_json)

    def create_from_json(self, repo, webhook_json):
        data = self.serialize(webhook_json)
        data.update({'repo': repo})
        return self.create(**data)

    def update_or_create_from_json(self, repo, webhook_json):
        Webhook = apps.get_model('github.Webhook')
        github_id = webhook_json['github_id']
        try:
            webhook = self.get(github_id=github_id, repo=repo)
            webhook.update_from_json(webhook_json)
            return webhook
        except Webhook.DoesNotExist:
            return self.create_from_json(repo, webhook_json)

    def serialize(self, webhook_json):
        return serialize_github_webhook(webhook_json)
