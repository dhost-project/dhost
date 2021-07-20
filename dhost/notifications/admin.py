from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("subject", "user", "timestamp")
    search_fields = ("user__username", "subject")
    list_filter = ("read", "timestamp")
