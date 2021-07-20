# Generated by Django 3.2.4 on 2021-06-25 13:56

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("dapps", "0002_alter_dapp_created_at"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="APILog",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("object_id", models.TextField(blank=True, null=True)),
                (
                    "action_flag",
                    models.CharField(
                        choices=[
                            ("other", "Other"),
                            ("dapp_add", "Dapp created"),
                            ("dapp_change", "Dapp updated"),
                            ("auto_deploy_start", "Auto deployment started"),
                            ("deploy_start", "Deployment started"),
                            ("deploy_success", "Deployment successful"),
                            ("deploy_fail", "Deployment failed"),
                            ("build_opt_add", "Build options created"),
                            ("build_opt_change", "Build options updated"),
                            ("build_opt_del", "Build options removed"),
                            ("auto_build_start", "Auto build started"),
                            ("build_start", "Build started"),
                            ("build_success", "Build successful"),
                            ("build_fail", "Build failed"),
                            ("env_var_add", "New environment variable"),
                            ("env_var_change", "Environment variable updated"),
                            ("env_var_del", "Environment variable removed"),
                            ("github_opt_add", "Github options created"),
                            ("github_opt_change", "Github options changed"),
                            ("github_opt_del", "Github options removed"),
                        ],
                        default="other",
                        max_length=20,
                    ),
                ),
                ("change_message", models.TextField(blank=True)),
                (
                    "action_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "dapp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        related_query_name="logs",
                        to="dapps.dapp",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "API log entry",
                "verbose_name_plural": "API log entries",
                "ordering": ["-action_time"],
            },
        ),
    ]
