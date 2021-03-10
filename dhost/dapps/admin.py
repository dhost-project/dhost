from django.contrib import admin

from .models import Dapp


@admin.register(Dapp)
class DappAdmin(admin.ModelAdmin):
    pass
