from django.contrib import admin

from .models import DashboardLogEntry


@admin.register(DashboardLogEntry)
class DashboardLogEntryAdmin(admin.ModelAdmin):
    pass
