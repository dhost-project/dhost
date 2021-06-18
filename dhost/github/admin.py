from django.contrib import admin

from .models import Branch, GithubOptions, Repository, Webhook


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    pass


@admin.register(GithubOptions)
class GithubOptionsAdmin(admin.ModelAdmin):
    pass
