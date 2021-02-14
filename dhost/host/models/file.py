from django.db import models

from .technology import Technology


class File(models.Model):
    name = models.CharField(max_length=128)
    technology = models.ForeignKey(
        Technology, on_delete=models.SET_NULL, null=True
    )
    url = models.URLField()
    content = models.TextField()
