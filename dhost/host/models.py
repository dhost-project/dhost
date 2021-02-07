from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=42)


class File(models.Model):
    name = models.CharField(max_length=128)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    content = models.TextField()


class Website(models.Model):

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

