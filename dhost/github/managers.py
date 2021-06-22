from django.apps import apps
from django.db import models

from .github import DjangoGithubAPI


def serialize_repository(repo_json):
    """Serialize from the Github API to a dict."""
    return {
        'id': repo_json['id'],
        'github_owner': repo_json['owner']['login'],
        'github_repo': repo_json['name'],
        'extra_data': repo_json,
    }


def serialize_branch(branch_json):
    return {
        'name': branch_json['name'],
        'extra_data': branch_json,
    }


def serialize_webhook(webhook_json):
    return {
        'id': webhook_json['id'],
        'name': webhook_json['name'],
        'active': webhook_json['active'],
        'extra_data': webhook_json,
    }


class RepositoryManager(models.Manager):

    def fetch_all(self, user):
        g = DjangoGithubAPI(user=user)
        repo_list = g.list_repos()
        for repo in repo_list:
            self.update_or_create_from_json(repo_json=repo, user=user)
        self.remove_unavailable_list(repo_list=repo_list, user=user)

    def remove_unavailable_list(self, repo_list, user):
        """
        Remove user from available repos if they are not present in the Github
        API `list_repos` response.
        """
        # Create a list of ID gathered during the Github API call
        repo_id_list = [r['id'] for r in repo_list]

        # Get all the user's repos
        Repository = apps.get_model('github.Repository')
        repo_obj_list = Repository.objects.filter(users=user)

        for repo_obj in repo_obj_list:
            # If the repo object is not present in the `repo_id_list` it's not
            # available anymore and thus the user should not be linked to that
            # repo anymore.
            if repo_obj.id not in repo_id_list:
                repo_obj.remove_user(user)

    def create_from_json(self, repo_json, user):
        """Create a `Repository` from a Github API response."""
        data = self.serialize(repo_json)
        repo = self.create(**data)
        repo.users.add(user)
        repo.save()
        return repo

    def update_or_create_from_json(self, repo_json, user):
        """
        Like get_or_create but from Github API response and update instead of
        just getting the object when it exist.
        """
        Repository = apps.get_model('github.Repository')
        try:
            github_repo = self.get(id=repo_json['id'])
            github_repo.update_from_json(repo_json, user)
            return github_repo
        except Repository.DoesNotExist:
            return self.create_from_json(repo_json, user)

    def serialize(self, repo_json):
        return serialize_repository(repo_json)


class BranchManager(models.Manager):

    def fetch_repo_branches(self, repo, user):
        # TODO remove branches that are not present in the response because
        # they are either deleted or inavailable
        g = DjangoGithubAPI(user=user)
        branch_list = g.list_branches(owner=repo.github_owner,
                                      repo=repo.github_repo)
        for branch in branch_list:
            self.update_or_create_from_json(repo, branch)
        self.remove_unavailable_list(branch_list, repo)
        return branch_list

    def remove_unavailable_list(self, branch_list, repo):
        """
        Check and remove branch from repo if it exist in the DB and not in the
        list.
        """
        # TODO
        pass

    def remove_unavailable(self, branch, repo):
        """Remove branch from repo."""
        # TODO
        pass

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
        return serialize_branch(branch_json)


class WebhookManager(models.Manager):

    def create_github_webhook(self, repo, owner, name='web'):
        g = DjangoGithubAPI()
        webhook_json = g.create_webhook(owner=owner, repo=repo, name=name)
        return self.create_from_json(repo=repo, webhook_json=webhook_json)

    def create_from_json(self, webhook_json, repo):
        data = self.serialize(webhook_json)
        data.update({'repo': repo})
        return self.create(**data)

    def update_or_create_from_json(self, webhook_json, repo):
        Webhook = apps.get_model('github.Webhook')
        try:
            webhook = self.get(id=webhook_json['id'], repo=repo)
            webhook.update_from_json(webhook_json)
            return webhook
        except Webhook.DoesNotExist:
            return self.create_from_json(webhook_json, repo)

    def serialize(self, webhook_json):
        return serialize_webhook(webhook_json)
