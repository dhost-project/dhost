# Generated by Django 3.1.6 on 2021-03-11 09:13

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('builds', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dapp',
            fields=[
                ('buildoptions_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='builds.buildoptions')),
                ('name', models.CharField(error_messages={'unique': 'A dapp with that name already exists.'}, max_length=128, unique=True, verbose_name='dapp name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('url', models.CharField(blank=True, max_length=2048, verbose_name='URL')),
                ('status', models.CharField(choices=[('SO', 'Stoped'), ('BI', 'Building'), ('BT', 'Builed'), ('DP', 'Deploying'), ('SA', 'Starting'), ('UP', 'Running'), ('UA', 'Unavailable'), ('ER', 'Error')], default='SO', max_length=2, verbose_name='status')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='created')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dapps', related_query_name='dapps', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'dapp',
                'verbose_name_plural': 'dapps',
                'abstract': False,
            },
            bases=('builds.buildoptions', models.Model),
        ),
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('folder', models.FilePathField(allow_folders=True, blank=True, null=True, verbose_name='folder')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('build', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bundles', related_query_name='bundles', to='builds.build', verbose_name='build')),
                ('dapp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bundles', related_query_name='bundles', to='dapps.dapp', verbose_name='dapp')),
            ],
            options={
                'verbose_name': 'bundle',
                'verbose_name_plural': 'bundles',
            },
        ),
    ]