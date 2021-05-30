from django.contrib import admin

from .models import GithubRepository, GithubCommit


@admin.register(GithubRepository)
class GithubRepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(GithubCommit)
class GithubCommit(admin.ModelAdmin):
    pass
