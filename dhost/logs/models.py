import uuid

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Dapp

DAPP_ADDITION = 1
DAPP_CHANGE = 2
AUTO_DEPLOY_START = 4
DEPLOY_START = 5
DEPLOY_SUCCESS = 6
DEPLOY_FAIL = 7
BUILD_OPTIONS_ADDITION = 8
BUILD_OPTIONS_CHANGE = 9
BUILD_OPTIONS_DELETION = 10
AUTO_BUILD_START = 11
BUILD_START = 12
BUILD_SUCCESS = 13
BUILD_FAIL = 14
ENV_VAR_ADDITION = 15
ENV_VAR_CHANGE = 16
ENV_VAR_DELETION = 17

ACTION_FLAG_CHOICES = (
    (DAPP_ADDITION, _('Dapp created')),
    (DAPP_CHANGE, _('Dapp updated')),
    (AUTO_DEPLOY_START, _('Auto deployment started')),
    (DEPLOY_START, _('Deployment started')),
    (DEPLOY_SUCCESS, _('Deployment successful')),
    (DEPLOY_FAIL, _('Deployment failed')),
    (BUILD_OPTIONS_ADDITION, _('Build options created')),
    (BUILD_OPTIONS_CHANGE, _('Build options updated')),
    (BUILD_OPTIONS_DELETION, _('Build options removed')),
    (AUTO_BUILD_START, _('Auto build started')),
    (BUILD_START, _('Build started')),
    (BUILD_SUCCESS, _('Build successful')),
    (BUILD_FAIL, _('Build failed')),
    (ENV_VAR_ADDITION, _('New environment variable')),
    (ENV_VAR_CHANGE, _('Environment variable updated')),
    (ENV_VAR_DELETION, _('Environment variable removed')),
)


class APILog(models.Model):
    """
    API log entry, each state changing command (POST, PUT, PATCH, DELETE) sent
    to the API server is recorded in the form of an APILog object.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dapp = models.ForeignKey(Dapp,
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
        verbose_name = _('API log entry')
        verbose_name_plural = _('API log entries')
        ordering = ['-action_time']

    def __str__(self):
        return self.change_message
