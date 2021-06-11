from rest_framework import serializers

from .models import Branch, Repository


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = ['id', 'github_owner', 'github_repo', 'added_at', 'updated_at']
        read_only_fields = [
            'id', 'github_owner', 'github_repo', 'added_at', 'updated_at'
        ]


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = ['name']
