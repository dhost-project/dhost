from django.contrib import admin

from .models import Dapp, DappGithubRepo, Deployment


@admin.register(Dapp)
class DappAdmin(admin.ModelAdmin):
    pass


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    pass


@admin.register(DappGithubRepo)
class DappGithubRepoAdmin(admin.ModelAdmin):
    pass
