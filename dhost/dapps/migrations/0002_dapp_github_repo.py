# Generated by Django 3.2.4 on 2021-06-10 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0002_auto_20210610_0715'),
        ('dapps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dapp',
            name='github_repo',
            field=models.ForeignKey(blank=True,
                                    null=True,
                                    on_delete=django.db.models.deletion.CASCADE,
                                    to='github.githubrepo'),
        ),
    ]
