from dhost.utils.env import env, env_bool, env_int

from .defaults import *  # noqa

DEBUG = False

SECRET_KEY = env("DJANGO_SECRET_KEY")

ENABLE_SSL = env_bool("ENABLE_SSL", True)

SECURE_SSL_REDIRECT = ENABLE_SSL

CSRF_COOKIE_SECURE = ENABLE_SSL

SESSION_COOKIE_SECURE = ENABLE_SSL

SECURE_HSTS_SECONDS = env_int("SECURE_HSTS_SECONDS", 60)

SECURE_HSTS_INCLUDE_SUBDOMAINS = ENABLE_SSL

SECURE_HSTS_PRELOAD = ENABLE_SSL

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
