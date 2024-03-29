from django.contrib import admin

from .models import Build, BuildOptions, EnvVar


@admin.register(BuildOptions)
class BuildOptionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(EnvVar)
class EnvVarAdmin(admin.ModelAdmin):
    pass
