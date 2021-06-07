# Generated by Django 3.2.2 on 2021-06-07 08:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_environmentvariable_unique variable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='environmentvariable',
            name='options',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                    related_name='envvars',
                                    to='builds.buildoptions'),
        ),
    ]
