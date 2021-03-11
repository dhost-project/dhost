# Generated by Django 3.1.6 on 2021-03-11 12:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ipfsdapp',
            options={'verbose_name': 'IPFS Dapp', 'verbose_name_plural': 'IPFS Dapps'},
        ),
        migrations.AlterModelOptions(
            name='ipfsdeployment',
            options={'verbose_name': 'IPFS Deployment', 'verbose_name_plural': 'IPFS Deployments'},
        ),
        migrations.RemoveField(
            model_name='ipfsdeployment',
            name='dapp',
        ),
        migrations.AlterField(
            model_name='ipfsdeployment',
            name='end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ipfsdeployment',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
