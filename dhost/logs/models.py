import uuid

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Dapp

ENV_VAR_ADDITION = 1
ENV_VAR_CHANGE = 2
ENV_VAR_DELETION = 3
START_BUILD = 4
BUILD_SUCCESS = 5
BUILD_FAIL = 6
START_DEPLOY = 7
DEPLOY_SUCCESS = 8
DEPLOY_FAIL = 9

ACTION_FLAG_CHOICES = (
    (ENV_VAR_ADDITION, _('New environment variable')),
    (ENV_VAR_CHANGE, _('Environment variable updated')),
    (ENV_VAR_DELETION, _('Environment variable removed')),
    (START_BUILD, _('Start build')),
    (BUILD_SUCCESS, _('Build successful')),
    (BUILD_FAIL, _('Build failed')),
    (START_DEPLOY, _('Start deployment')),
    (DEPLOY_SUCCESS, _('Deployment successful')),
    (DEPLOY_FAIL, _('Deployment failed')),
)


class APILog(models.Model):
    """
    API log entry, each state changing command (POST, PUT, PATCH, DELETE) sent
    to the API server it is recorded in the form of an APILog object.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    options = models.ForeignKey(Dapp,
                                on_delete=models.CASCADE,
                                related_name='logs',
                                related_query_name='logs')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    object_id = models.TextField(null=True, blank=True)
    action_flag = models.PositiveSmallIntegerField(
        choices=ACTION_FLAG_CHOICES,
        null=True,
        blank=True,
    )
    change_message = models.TextField(blank=True)
    action_time = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = _('dashboard log entry')
        verbose_name_plural = _('dashboard log entries')
        ordering = ['-action_time']

    def __str__(self):
        return self.change_message
