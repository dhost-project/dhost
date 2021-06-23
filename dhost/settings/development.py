from django.core.management.utils import get_random_secret_key

from .defaults import *  # noqa

SECRET_KEY = get_random_secret_key()

CORS_ALLOW_ALL_ORIGINS = True

# login on browsabler api
REST_FRAMEWORK['DEFAULT_AUTHENTICATION_CLASSES'].append(  # noqa
    'rest_framework.authentication.SessionAuthentication',)

# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/
ENABLE_DEBUG_TOOLBAR = True

INSTALLED_APPS.append('debug_toolbar')  # noqa

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')  # noqa


# To work with Docker
# https://stackoverflow.com/questions/26898597/django-debug-toolbar-and-docker
def show_toolbar(request):
    return True  # pragma: no cover


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}
