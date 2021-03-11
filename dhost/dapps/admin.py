from django.contrib import admin

from .models import Bundle, Dapp


@admin.register(Dapp)
class DappAdmin(admin.ModelAdmin):
    pass


@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    pass
