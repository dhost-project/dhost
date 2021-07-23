import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from dhost import __version__

from .defaults import *  # noqa

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

if env("ENABLE_SSL", "1") == "1":  # noqa

    SECURE_SSL_REDIRECT = True

    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = int(env("SECURE_HSTS_SECONDS", 60))  # noqa

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

# Redis
REDIS_URL = env("REDIS_URL")  # noqa

if REDIS_URL:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": REDIS_URL,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": True,
            },
        }
    }

    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

    SESSION_CACHE_ALIAS = "default"

# AWS S3
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")  # noqa

AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")  # noqa

AWS_DEFAULT_ACL = env("AWS_DEFAULT_ACL", None)  # noqa

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")  # noqa

AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", None)  # noqa

AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", None)  # noqa

AWS_LOCATION = env("AWS_LOCATION", "")  # noqa

AWS_MEDIA_BUCKET_NAME = env("AWS_MEDIA_BUCKET_NAME")  # noqa

AWS_MEDIA_CUSTOM_DOMAIN = env("AWS_MEDIA_CUSTOM_DOMAIN")  # noqa

# Google Cloud Storage
# https://cloud.google.com/storage/docs/access-control/making-data-public
# https://django-storages.readthedocs.io/en/latest/backends/gcloud.html
GS_BUCKET_NAME = env("GS_BUCKET_NAME", None)  # noqa

GS_PROJECT_ID = env("GS_PROJECT_ID")  # noqa

GS_CREDENTIALS = env("GS_CREDENTIALS")  # noqa

GS_DEFAULT_ACL = env("GS_DEFAULT_ACL")  # noqa

GS_QUERYSTRING_AUTH = env("GS_QUERYSTRING_AUTH", False)  # noqa

GS_LOCATION = env("GS_LOCATION", "")  # noqa

GS_MEDIA_BUCKET_NAME = env("GS_MEDIA_BUCKET_NAME", GS_BUCKET_NAME)  # noqa

# set the staticfiles storage to 'aws', 'google' or 'whitenoise'
DJANGO_STATICFILES_STORAGE = env(  # noqa
    "DJANGO_STATICFILES_STORAGE", "whitenoise"
)

if DJANGO_STATICFILES_STORAGE == "aws":
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3ManifestStaticStorage"
elif DJANGO_STATICFILES_STORAGE == "google":
    # TODO replace with a custom GCManifestStaticStorage
    STATICFILES_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
elif DJANGO_STATICFILES_STORAGE == "whitenoise":
    STATICFILES_STORAGE = (
        "whitenoise.storage." "CompressedManifestStaticFilesStorage"
    )
else:
    raise Exception(
        "DJANGO_STATICFILES_STORAGE not configured correctly, use one of: "
        "aws, google, whitenoise. default=whitenoise."
    )

# set the default storage to 'aws', 'google' or 'default'
DJANGO_DEFAULT_FILE_STORAGE = env("DEFAULT_FILE_STORAGE", "default")  # noqa

if DJANGO_DEFAULT_FILE_STORAGE == "aws":
    DEFAULT_FILE_STORAGE = "dhost.core.storages.S3Boto3MediaStorage"
elif DJANGO_DEFAULT_FILE_STORAGE == "google":
    DEFAULT_FILE_STORAGE = "dhost.code.storage.GoogleCloudMediaStorage"
elif DJANGO_DEFAULT_FILE_STORAGE != "default":
    raise Exception(
        "DJANGO_DEFAULT_FILE_STORAGE not configured correctly, use one of: "
        "aws, google, default. default=default."
    )

# Sentry
# https://docs.sentry.io/platforms/python/guides/django/
SENTRY_DSN = env("SENTRY_DSN")  # noqa

SENTRY_TRACES_SAMPLE_RATE = env("SENTRY_TRACES_SAMPLE_RATE", 1.0)  # noqa

SENTRY_SEND_DEFAULT_PII = env("SENTRY_SEND_DEFAULT_PII", True)  # noqa

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=SENTRY_TRACES_SAMPLE_RATE,
        send_default_pii=SENTRY_SEND_DEFAULT_PII,
        release=__version__,
    )
