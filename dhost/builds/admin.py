from django.contrib import admin

from .models import Build, BuildOptions, Bundle, EnvironmentVariable


@admin.register(BuildOptions)
class BuildOptionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Build)
class BuildAdmin(admin.ModelAdmin):
    pass


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    pass


@admin.register(EnvironmentVariable)
class EnvironmentVariableAdmin(admin.ModelAdmin):
    pass
