from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class LogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dhost.logs'
    app_label = 'logs'
    verbose_name = _('API logs')
