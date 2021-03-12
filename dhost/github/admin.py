from django.contrib import admin

from .models import Github, GithubCommit


@admin.register(Github)
class GithubAdmin(admin.ModelAdmin):
    pass


@admin.register(GithubCommit)
class GithubCommit(admin.ModelAdmin):
    pass
