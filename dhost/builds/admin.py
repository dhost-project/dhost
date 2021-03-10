from django.contrib import admin

from .models import Build, BuildOptions, EnvironmentVariable


@admin.register(BuildOptions)
class BuildOptions(admin.ModelAdmin):
    pass


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(EnvironmentVariable)
class EnvironmentVariableAdmin(admin.ModelAdmin):
    pass
