from django.db import models

from .file import File


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
    url = models.URLField()
    files = models.ManyToManyField(File, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
