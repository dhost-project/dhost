# Generated by Django 3.1.6 on 2021-03-10 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oauth2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='oauth2_provider_app_logos/'),
        ),
    ]
