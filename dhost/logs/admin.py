from django.contrib import admin

from .models import APILog


@admin.register(APILog)
class APILogAdmin(admin.ModelAdmin):
    pass
