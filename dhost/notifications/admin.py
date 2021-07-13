from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'time')
    search_fields = ('user__username', 'subject')
    list_filter = ('read',)
    ordering = ('-time',)
