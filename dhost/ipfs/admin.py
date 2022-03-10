from django.contrib import admin

from dhost.dapps.admin import DappAdmin, DeploymentAdmin

from .models import IPFSDapp, IPFSDeployment,IPFSFile

def send_file_to_ipfs(modeladmin, request, queryset):
    for obj in queryset:
        obj.upload_to_ipfs()

@admin.register(IPFSFile)
class IPFSFileAdmin(admin.ModelAdmin):
    actions =[send_file_to_ipfs]


@admin.register(IPFSDapp)
class IPFSDappAdmin(DappAdmin):
    pass


@admin.register(IPFSDeployment)
class IPFSDeploymentAdmin(DeploymentAdmin):
    pass
