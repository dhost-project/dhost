import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .defaults import *  # noqa

DEBUG = False

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

CORS_ALLOW_ALL_ORIGINS = False

if env('ENABLE_SSL', '1') == '1':  # noqa

    SECURE_SSL_REDIRECT = True

    CSRF_COOKIE_SECURE = True

    SESSION_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = int(env('SECURE_HSTS_SECONDS', 60))  # noqa

    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    SECURE_HSTS_PRELOAD = True

# Redis
REDIS_URL = env('REDIS_URL')  # noqa

if REDIS_URL:

    CACHES = {
        'default': {
            'BACKEND': 'django_redis.cache.RedisCache',
            'LOCATION': REDIS_URL,
            'OPTIONS': {
                'CLIENT_CLASS': 'django_redis.client.DefaultClient',
                'IGNORE_EXCEPTIONS': True,
            },
        }
    }

    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

    SESSION_CACHE_ALIAS = 'default'

# AWS S3
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')  # noqa

AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')  # noqa

AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL', None)  # noqa

AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')  # noqa

AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', None)  # noqa

AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', None)  # noqa

AWS_LOCATION = env('AWS_LOCATION', '')  # noqa

AWS_MEDIA_BUCKET_NAME = env('AWS_MEDIA_BUCKET_NAME')  # noqa

AWS_MEDIA_CUSTOM_DOMAIN = env('AWS_MEDIA_CUSTOM_DOMAIN')  # noqa

if AWS_STORAGE_BUCKET_NAME:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if AWS_MEDIA_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'dhost.core.storages.S3MediaStorage'

# Sentry
SENTRY_DSN = env('SENTRY_DSN')  # noqa

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )
