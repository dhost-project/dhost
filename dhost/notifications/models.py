from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
        related_query_name='notifications',
    )
    subject = models.CharField(_('subject'), max_length=200)
    content = models.TextField(_('content'), max_length=10000)
    read = models.BooleanField(_('read'), default=False)
    url = models.URLField(_('URL'), null=True, blank=True)
    time = models.DateTimeField(_('time'), auto_now_add=True)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

    def __str__(self):
        return self.subject
