from django.contrib import admin

from .models import Technology


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass
