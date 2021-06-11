from django.contrib import admin

from .models import Branch, Repository, Webhook


@admin.register(Repository)
class RepositoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass


@admin.register(Webhook)
class WebhookAdmin(admin.ModelAdmin):
    pass
