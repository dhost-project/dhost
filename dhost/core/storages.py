from django.conf import settings
from storages.backends.gcloud import GoogleCloudStorage
from storages.backends.s3boto3 import S3Boto3Storage


class S3Boto3MediaStorage(S3Boto3Storage):
    bucket_name = settings.AWS_MEDIA_BUCKET_NAME
    custom_domain = settings.AWS_MEDIA_CUSTOM_DOMAIN


class GoogleCloudMediaStorage(GoogleCloudStorage):
    bucket_name = settings.GS_MEDIA_BUCKET_NAME
