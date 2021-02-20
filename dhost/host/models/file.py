from django.conf import settings
from django.db import models

from .technology import Technology

User = settings.AUTH_USER_MODEL


class File(models.Model):
    name = models.CharField(max_length=128)
    owner = models.ForeignKey(User, related_name='files', on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    content = models.TextField()
