from django.contrib import admin

from .models import IPFSDapp


@admin.register(IPFSDapp)
class IPFSDappAdmin(admin.ModelAdmin):
    pass
