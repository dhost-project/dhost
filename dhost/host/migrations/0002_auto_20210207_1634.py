# Generated by Django 3.1.6 on 2021-02-07 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("host", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("url", models.URLField()),
                ("content", models.TextField()),
                (
                    "technology",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="host.technology",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="website",
            name="files",
            field=models.ManyToManyField(blank=True, to="host.File"),
        ),
    ]
