from django.contrib import admin

from dhost.dapps.admin import DappAdmin, DeploymentAdmin

from .models import IPFSDapp, IPFSDeployment


@admin.register(IPFSDapp)
class IPFSDappAdmin(DappAdmin):
    pass


@admin.register(IPFSDeployment)
class IPFSDeploymentAdmin(DeploymentAdmin):
    pass
