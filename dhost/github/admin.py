from django.contrib import admin

from .models import GithubRepo


@admin.register(GithubRepo)
class GithubRepoAdmin(admin.ModelAdmin):
    pass
