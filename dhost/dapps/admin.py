from django.contrib import admin

from .models import Bundle, Dapp, Deployment

def deploy(modeladmin, request, queryset):
    for obj in queryset:
        obj.deploy()

@admin.register(Dapp)
class DappAdmin(admin.ModelAdmin):
    actions = [deploy]


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    pass


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    pass
