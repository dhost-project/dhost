# Generated by Django 3.2.4 on 2021-06-19 11:39

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dapps', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                (
                    'updated_at',
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text='Last updated from the Github API.',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                (
                    'id',
                    models.IntegerField(
                        help_text='Github repository unique ID.',
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name='Github ID',
                    ),
                ),
                ('github_owner', models.CharField(max_length=256)),
                ('github_repo', models.CharField(max_length=256)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                (
                    'added_at',
                    models.DateTimeField(auto_now_add=True,
                                         help_text='Added at.'),
                ),
                (
                    'updated_at',
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text='Last updated from the Github API.',
                    ),
                ),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Github repository',
                'verbose_name_plural': 'Github repositories',
            },
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                (
                    'id',
                    models.IntegerField(
                        help_text='Github webhook unique ID.',
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name='Github ID',
                    ),
                ),
                ('name', models.CharField(default='web', max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('extra_data', models.JSONField(blank=True, default=dict)),
                (
                    'added_at',
                    models.DateTimeField(auto_now_add=True,
                                         help_text='Added at.'),
                ),
                (
                    'updated_at',
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        help_text='Last updated from the Github API.',
                    ),
                ),
                (
                    'last_called_at',
                    models.DateTimeField(
                        blank=True,
                        help_text='Last called by Github.',
                        null=True,
                    ),
                ),
                (
                    'repo',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='webhooks',
                        related_query_name='webhooks',
                        to='github.repository',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Github webhook',
                'verbose_name_plural': 'Github webhooks',
            },
        ),
        migrations.CreateModel(
            name='GithubOptions',
            fields=[
                (
                    'dapp',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to='dapps.dapp',
                    ),
                ),
                (
                    'auto_deploy',
                    models.BooleanField(
                        default=False,
                        help_text='Automatically deploy the dapp when a push '
                        'is made on the selected branch.',
                    ),
                ),
                (
                    'confirm_ci',
                    models.BooleanField(
                        default=False,
                        help_text='Wait for CI to pass before automatically '
                        'deploying the dapp.',
                    ),
                ),
                (
                    'branch',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='github.branch',
                    ),
                ),
                (
                    'repo',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='github.repository',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Dapp Github options',
                'verbose_name_plural': 'Dapps Github options',
            },
        ),
        migrations.AddField(
            model_name='branch',
            name='repo',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='branches',
                related_query_name='branches',
                to='github.repository',
            ),
        ),
    ]
