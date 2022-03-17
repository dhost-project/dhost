from django.contrib import admin

from dhost.dapps.admin import DappAdmin, DeploymentAdmin

from .models import IPFSDapp, IPFSDeployment


def send_to_ipfs(modeladmin, request, queryset):
    for obj in queryset:
        obj.create_deployment()


@admin.register(IPFSDapp)
class IPFSDappAdmin(DappAdmin):
    actions = [send_to_ipfs]


@admin.register(IPFSDeployment)
class IPFSDeploymentAdmin(DeploymentAdmin):
    pass
