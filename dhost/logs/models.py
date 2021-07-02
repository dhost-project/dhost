import uuid

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from dhost.dapps.models import Dapp


class ActionFlags(models.TextChoices):
    OTHER = 'other', _('Other')
    DAPP_ADDITION = 'dapp_add', _('Dapp created')
    DAPP_CHANGE = 'dapp_change', _('Dapp updated')
    BUNDLE_ADDITION = 'bundle_add', _('Bundle added')
    BUNDLE_DELETION = 'bundle_del', _('Bundle removed')
    AUTO_DEPLOY_START = 'auto_deploy_start', _('Auto deployment started')
    DEPLOY_START = 'deploy_start', _('Deployment started')
    DEPLOY_SUCCESS = 'deploy_success', _('Deployment successful')
    DEPLOY_FAIL = 'deploy_fail', _('Deployment failed')
    BUILD_OPTIONS_ADDITION = 'build_opt_add', _('Build options created')
    BUILD_OPTIONS_CHANGE = 'build_opt_change', _('Build options updated')
    BUILD_OPTIONS_DELETION = 'build_opt_del', _('Build options removed')
    AUTO_BUILD_START = 'auto_build_start', _('Auto build started')
    BUILD_START = 'build_start', _('Build started')
    BUILD_SUCCESS = 'build_success', _('Build successful')
    BUILD_FAIL = 'build_fail', _('Build failed')
    ENV_VAR_ADDITION = 'env_var_add', _('New environment variable')
    ENV_VAR_CHANGE = 'env_var_change', _('Environment variable updated')
    ENV_VAR_DELETION = 'env_var_del', _('Environment variable removed')
    GITHUB_OPTIONS_ADDITION = 'github_opt_add', _('Github options created')
    GITHUB_OPTIONS_CHANGE = 'github_opt_change', _('Github options changed')
    GITHUB_OPTIONS_DELETION = 'github_opt_del', _('Github options removed')


class APILog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dapp = models.ForeignKey(
        Dapp,
        on_delete=models.CASCADE,
        related_name='logs',
        related_query_name='logs',
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    object_id = models.TextField(null=True, blank=True)
    action_flag = models.CharField(
        max_length=20,
        choices=ActionFlags.choices,
        default=ActionFlags.OTHER,
    )
    change_message = models.TextField(blank=True)
    action_time = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = _('API log entry')
        verbose_name_plural = _('API log entries')
        ordering = ['-action_time']

    def __str__(self):
        return self.change_message
