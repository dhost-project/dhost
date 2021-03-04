# AWS Bucket setup

## Env vars

| Environment variables | Prod | Default values | Descriptions |
| --- | --- | --- | --- |
| `AWS_ACCESS_KEY_ID` | ❓ | | AWS access key more infos [here](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) |
| `AWS_SECRET_ACCESS_KEY` | ❓ | | AWS secret key |
| `AWS_DEFAULT_ACL` | ❓ | `None` | AWS ACL |
| `AWS_STORAGE_BUCKET_NAME` | ❓ | | AWS bucket name, giving a storage bucket name will enable storage of staticfiles |
| `AWS_S3_CUSTOM_DOMAIN` | ❓ | | Custom domain for static bucket |
| `AWS_MEDIA_BUCKET_NAME` | ❓ | | AWS bucket name, giving a media bucket name will enable storage of media files |
| `AWS_MEDIA_CUSTOM_DOMAIN` | ❓ | | Custom domain for media bucket |
| `STATIC_URL` | ❓ | `/static/` | For AWS: `https://<bucket_name>.s3.amazonaws.com/<static>/` |
| `AWS_LOCATION` | ❓ | | The base path inside you S3 bucket |
| `AWS_S3_REGION_NAME` | ❓ | | AWS region name |
