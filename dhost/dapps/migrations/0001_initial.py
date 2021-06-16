# Generated by Django 3.2.4 on 2021-06-16 21:07

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import dhost.dapps.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4,
                                  editable=False,
                                  primary_key=True,
                                  serialize=False)),
                ('folder',
                 models.FilePathField(allow_folders=True,
                                      blank=True,
                                      null=True,
                                      path=dhost.dapps.models.bundle_path,
                                      verbose_name='folder')),
                ('created_at',
                 models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'bundle',
                'verbose_name_plural': 'bundles',
            },
        ),
        migrations.CreateModel(
            name='Dapp',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('slug',
                 models.SlugField(help_text='[A-Za-z0-9_-]',
                                  max_length=256,
                                  verbose_name='dapp name')),
                ('url',
                 models.CharField(blank=True,
                                  max_length=2048,
                                  verbose_name='URL')),
                ('status',
                 models.CharField(choices=[
                     ('SO', 'Stoped'), ('BI', 'Building'), ('BT', 'Builed'),
                     ('DP', 'Deploying'), ('SA', 'Starting'), ('UP', 'Running'),
                     ('UA', 'Unavailable'), ('ER', 'Error')
                 ],
                                  default='SO',
                                  max_length=2,
                                  verbose_name='status')),
                ('created_at',
                 models.DateTimeField(default=django.utils.timezone.now,
                                      verbose_name='created')),
                ('owner',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='dapps_dapp',
                                   related_query_name='dapps_dapp',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='owner')),
            ],
            options={
                'verbose_name': 'dapp',
                'verbose_name_plural': 'dapps',
            },
        ),
        migrations.CreateModel(
            name='Deployment',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4,
                                  editable=False,
                                  primary_key=True,
                                  serialize=False)),
                ('status',
                 models.CharField(choices=[('SO', 'Stoped'),
                                           ('DP', 'Deploying'),
                                           ('SA', 'Starting'),
                                           ('UP', 'Running'),
                                           ('UA', 'Unavailable')],
                                  default='SO',
                                  max_length=2)),
                ('start',
                 models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('bundle',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='deployments',
                                   related_query_name='deployments',
                                   to='dapps.bundle')),
                ('dapp',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='deployments',
                                   related_query_name='deployments',
                                   to='dapps.dapp')),
            ],
            options={
                'verbose_name': 'deployment',
                'verbose_name_plural': 'deployments',
            },
        ),
        migrations.AddField(
            model_name='bundle',
            name='dapp',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    related_name='bundles',
                                    related_query_name='bundles',
                                    to='dapps.dapp'),
        ),
        migrations.AddConstraint(
            model_name='dapp',
            constraint=models.UniqueConstraint(fields=('owner', 'slug'),
                                               name='dapps_dapp_unique_slug'),
        ),
    ]
