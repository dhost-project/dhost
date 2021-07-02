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
        """Update every user's repositories.

        Create if they don't exist, update them if they do, and remove the user
        form the repo if it's not available anymore.
        """
        g = DjangoGithubAPI(user=user)
        repo_list = g.list_repos()
        for repo in repo_list:
            self.update_or_create_from_json(repo_json=repo, user=user)
        self.remove_unavailable_list(repo_list=repo_list, user=user)

    def remove_unavailable_list(self, repo_list, user):
        """Remove user from available repos.

        Remove if they are not present in the Github API `list_repos` response.

        Args:
            repo_list (list): a list of repos returned by the Github API.
            user (User): the user to remove from inavailable repos.
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
                self.remove_unavailable(repo=repo_obj, user=user)

    def remove_unavailable(self, repo, user):
        repo.remove_user(user)

    def create_from_json(self, repo_json, user):
        """Create a `Repository` from a Github API response."""
        data = self.serialize(repo_json)
        repo = self.create(**data)
        repo.users.add(user)
        repo.save()
        return repo

    def update_or_create_from_json(self, repo_json, user):
        """Like get_or_create but from Github API response.

        Uupdate instead of just getting the object when it exist.
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
        g = DjangoGithubAPI(user=user)
        branch_list = g.list_branches(owner=repo.github_owner,
                                      repo=repo.github_repo)
        for branch in branch_list:
            self.update_or_create_from_json(repo, branch)
        self.remove_unavailable_list(branch_list, repo)

    def remove_unavailable_list(self, branch_list, repo):
        """Remove unavailable objects from a list.

        Check and remove branch from repo if it exist as object and is not in
        the list.

        Args:
            branch_list (list): a list of branches returned by the Github API.
            repo (Repository): a repo object.
        """
        # Create a list of branches name gathered during the Github API call
        branch_name_list = [r['name'] for r in branch_list]

        # Get all the repo's branches
        branch_obj_list = repo.branches.all()

        for branch_obj in branch_obj_list:
            # If the branch object is not present in the `branch_name_list`
            # it's not available anymore and thus the branch should be deleted
            if branch_obj.name not in branch_name_list:
                self.remove_unavailable(branch_obj)

    def remove_unavailable(self, branch):
        return branch.delete()

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

    def create_webhook(self, repo, user, name='web'):
        g = DjangoGithubAPI(user=user)
        webhook_json = g.create_hook(owner=repo.github_owner,
                                     repo=repo.github_repo,
                                     name=name)
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
