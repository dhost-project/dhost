# Generated by Django 4.0.3 on 2022-03-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapps', '0005_alter_dapp_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='media/ipfs'),
        ),
    ]
