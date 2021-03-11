from django.contrib import admin

from .models import IPFSDapp, IPFSDeployment


@admin.register(IPFSDapp)
class IPFSDappAdmin(admin.ModelAdmin):
    pass


@admin.register(IPFSDeployment)
class IPFSDeploymentAdmin(admin.ModelAdmin):
    pass
