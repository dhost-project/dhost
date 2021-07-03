from django.core.management.utils import get_random_secret_key

from .defaults import *  # noqa

SECRET_KEY = get_random_secret_key()

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True

# login on browsabler api
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(  # noqa
    'rest_framework.authentication.SessionAuthentication',)
