# Generated by Django 3.2.4 on 2021-06-16 21:29

import uuid

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import dhost.builds.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dapps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildOptions',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4,
                                  editable=False,
                                  primary_key=True,
                                  serialize=False)),
                ('source',
                 models.FilePathField(allow_folders=True,
                                      blank=True,
                                      max_length=1024,
                                      null=True,
                                      path=dhost.builds.models.source_path,
                                      recursive=True,
                                      verbose_name='Source folder')),
                ('command',
                 models.CharField(
                     blank=True,
                     help_text='Command used during the build process.',
                     max_length=2048,
                     verbose_name='build command')),
                ('docker',
                 models.CharField(
                     blank=True,
                     help_text='Container used for the build process.',
                     max_length=128)),
            ],
            options={
                'verbose_name': 'build options',
                'verbose_name_plural': 'builds options',
            },
        ),
        migrations.CreateModel(
            name='EnvVar',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('variable', models.SlugField(max_length=1024)),
                ('value', models.CharField(max_length=8192)),
                ('options',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='envvars',
                                   to='builds.buildoptions')),
            ],
            options={
                'verbose_name': 'environment variable',
                'verbose_name_plural': 'environment variables',
            },
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id',
                 models.UUIDField(default=uuid.uuid4,
                                  editable=False,
                                  primary_key=True,
                                  serialize=False)),
                ('is_success',
                 models.BooleanField(blank=True,
                                     help_text='Based on the build return code',
                                     null=True)),
                ('logs',
                 models.TextField(
                     blank=True,
                     help_text='Raw logs output of the build process')),
                ('source_path',
                 models.FilePathField(allow_files=False,
                                      allow_folders=True,
                                      blank=True,
                                      help_text='Source folder',
                                      max_length=1024,
                                      null=True,
                                      path=dhost.builds.models.source_path,
                                      recursive=True)),
                ('start',
                 models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('bundle',
                 models.OneToOneField(
                     blank=True,
                     null=True,
                     on_delete=django.db.models.deletion.SET_NULL,
                     related_name='build',
                     related_query_name='build',
                     to='dapps.bundle',
                     verbose_name='bundle')),
                ('options',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='builds',
                                   related_query_name='builds',
                                   to='builds.buildoptions')),
            ],
            options={
                'verbose_name': 'build',
                'verbose_name_plural': 'builds',
            },
        ),
        migrations.AddConstraint(
            model_name='envvar',
            constraint=models.UniqueConstraint(fields=('options', 'variable'),
                                               name='unique variable'),
        ),
    ]
