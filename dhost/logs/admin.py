from django.contrib import admin

from .models import DappLog


@admin.register(DappLog)
class DappLogAdmin(admin.ModelAdmin):
    pass
