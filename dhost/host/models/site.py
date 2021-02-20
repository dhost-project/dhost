from django.conf import settings
from django.db import models

from .file import File

User = settings.AUTH_USER_MODEL


class Site(models.Model):

    STARTING = 'SR'
    WORKING = 'UP'
    STOPED = 'ST'
    UPDATING = 'UD'
    STATUS_CHOICES = [
        (STARTING, 'Starting'),
        (WORKING, 'Working'),
        (STOPED, 'Stoped'),
        (UPDATING, 'Updating'),
    ]

    name = models.CharField(max_length=42)
    owner = models.ForeignKey(User, related_name='sites', on_delete=models.CASCADE)
    url = models.URLField()
    files = models.ManyToManyField(File, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
