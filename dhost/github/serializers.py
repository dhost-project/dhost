from rest_framework import serializers

from .models import GithubRepo


class GithubRepoSerializer(serializers.ModelSerializer):

    class Meta:
        model = GithubRepo
        fields = [
            'id', 'name', 'branch', 'auto_deploy', 'github_owner',
            'github_repo', 'size', 'updated', 'created', 'modified'
        ]
        read_only_fields = [
            'id', 'name', 'github_owner', 'github_repo', 'size', 'updated',
            'created', 'modified'
        ]
