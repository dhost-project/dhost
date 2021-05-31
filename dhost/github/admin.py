from django.contrib import admin

from .models import GithubCommit, GithubRepository


@admin.register(GithubRepository)
class GithubRepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(GithubCommit)
class GithubCommit(admin.ModelAdmin):
    pass
