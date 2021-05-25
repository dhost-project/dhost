# Generated by Django 3.2b1 on 2021-05-18 09:20

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dapps', '0001_initial'),
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPFSDapp',
            fields=[
                ('dapp_ptr',
                 models.OneToOneField(
                     auto_created=True,
                     on_delete=django.db.models.deletion.CASCADE,
                     parent_link=True,
                     primary_key=True,
                     serialize=False,
                     to='dapps.dapp')),
                ('hash',
                 models.CharField(blank=True,
                                  max_length=128,
                                  verbose_name='IPFS hash')),
            ],
            options={
                'verbose_name': 'IPFS Dapp',
                'verbose_name_plural': 'IPFS Dapps',
                'abstract': False,
            },
            bases=('dapps.dapp',),
        ),
        migrations.CreateModel(
            name='IPFSDeployment',
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
                ('hash',
                 models.CharField(blank=True,
                                  max_length=128,
                                  verbose_name='IPFS hash')),
                ('bundle',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='deployments',
                                   related_query_name='deployments',
                                   to='builds.bundle')),
                ('dapp',
                 models.ForeignKey(null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   related_name='deployments',
                                   related_query_name='deployments',
                                   to='dapps.dapp')),
            ],
            options={
                'verbose_name': 'IPFS Deployment',
                'verbose_name_plural': 'IPFS Deployments',
                'abstract': False,
            },
        ),
    ]
