from django.core.management.utils import get_random_secret_key

from .defaults import *  # noqa

SECRET_KEY = get_random_secret_key()

DEBUG = True

# login on browsable api, note that views that require oauth scopes will return
# 403 anyway because the authentication will not be via the oauth provider
REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"].append(  # noqa
    "rest_framework.authentication.SessionAuthentication"
)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
