# Generated by Django 3.2.5 on 2021-07-13 14:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="notification",
            options={
                "ordering": ("-timestamp",),
                "verbose_name": "notification",
                "verbose_name_plural": "notifications",
            },
        ),
        migrations.RemoveField(
            model_name="notification",
            name="time",
        ),
        migrations.AddField(
            model_name="notification",
            name="level",
            field=models.CharField(
                choices=[
                    ("info", "info"),
                    ("success", "success"),
                    ("warning", "warning"),
                    ("error", "error"),
                ],
                default="info",
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name="notification",
            name="timestamp",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="timestamp"
            ),
        ),
    ]