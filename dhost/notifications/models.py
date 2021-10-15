import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timesince import timesince
from django.utils.translation import gettext_lazy as _


class NotificationQuerySet(models.query.QuerySet):
    def unread(self):
        return self.filter(read=False)

    def read(self):
        return self.filter(read=True)

    def mark_all_as_read(self):
        return self.unread().update(read=True)

    def mark_all_as_unread(self):
        return self.read().update(read=False)


class NotificationLevel(models.TextChoices):
    INFO = "info", _("info")
    SUCCESS = "success", _("success")
    WARNING = "warning", _("warning")
    ERROR = "error", _("error")


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
        related_query_name="notifications",
    )
    subject = models.CharField(_("subject"), max_length=200)
    content = models.TextField(_("content"), max_length=10000)
    level = models.CharField(
        choices=NotificationLevel.choices,
        default=NotificationLevel.INFO,
        max_length=10,
    )
    read = models.BooleanField(_("read"), default=False)
    url = models.URLField(_("URL"), null=True, blank=True)
    timestamp = models.DateTimeField(_("timestamp"), default=timezone.now)
    objects = NotificationQuerySet.as_manager()

    class Meta:
        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
        ordering = ("-timestamp",)

    def __str__(self):
        return f"{self.user} {self.subject} {self.timesince()} ago"

    def timesince(self, now=timezone.now()):
        return timesince(self.timestamp, now)

    def mark_as_read(self):
        if not self.read:
            self.read = True
            self.save()

    def mark_as_unread(self):
        if self.read:
            self.read = False
            self.save()
