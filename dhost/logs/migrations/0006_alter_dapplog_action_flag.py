# Generated by Django 4.0.3 on 2022-04-01 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logs", "0005_rename_apilog_dapplog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dapplog",
            name="action_flag",
            field=models.CharField(
                choices=[
                    ("other", "Other"),
                    ("dapp_add", "Dapp created"),
                    ("dapp_change", "Dapp updated"),
                    ("bundle_add", "Bundle added"),
                    ("auto_deploy_start", "Auto deployment started"),
                    ("deploy_start", "Deployment started"),
                    ("deploy_success", "Deployment successful"),
                    ("deploy_fail", "Deployment failed"),
                    ("build_opt_add", "Build options created"),
                    ("build_opt_change", "Build options updated"),
                    ("build_opt_del", "Build options removed"),
                    ("auto_build_start", "Auto build started"),
                    ("build_start", "Build started"),
                    ("build_success", "Build successful"),
                    ("build_fail", "Build failed"),
                    ("env_var_add", "New environment variable"),
                    ("env_var_change", "Environment variable updated"),
                    ("env_var_del", "Environment variable removed"),
                    ("github_opt_add", "Github options created"),
                    ("github_opt_change", "Github options changed"),
                    ("github_opt_del", "Github options removed"),
                ],
                default="other",
                max_length=20,
            ),
        ),
    ]
