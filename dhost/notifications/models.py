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
    subject = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    url = models.URLField(null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('notification')
        verbose_name_plural = _('notifications')

    def __str__(self):
        return self.subject
