from rest_framework import serializers

from .models import Branch, GithubOptions, Repository


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['name']
        read_only_fields = ['name']


class RepositorySerializer(serializers.ModelSerializer):

    branches = BranchSerializer(many=True)

    class Meta:
        model = Repository
        fields = [
            'id', 'github_owner', 'github_repo', 'branches', 'added_at',
            'updated_at'
        ]
        read_only_fields = [
            'id', 'github_owner', 'github_repo', 'branches', 'added_at',
            'updated_at'
        ]


class GithubOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GithubOptions
        fields = ['repo', 'branch', 'auto_deploy', 'confirm_ci']
