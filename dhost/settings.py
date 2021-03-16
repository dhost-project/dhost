import ast
import os
import warnings
from pathlib import Path

import dj_database_url
import sentry_sdk
from django.core.management.utils import get_random_secret_key
from sentry_sdk.integrations.django import DjangoIntegration


def env(var, default=None):
    return os.environ.get(var, default)


def env_bool(var, default=None):
    return ast.literal_eval(env(var, str(default)))


def env_list(var, default=None, separator=','):
    """Return a python list of value from env vars"""
    text_list = env(var, default)
    return [item.strip() for item in text_list.split(separator)]


BASE_DIR = Path(__file__).resolve().parent.parent

SITE_ID = env('SITE_ID', 1)

DEBUG = env_bool('DEBUG', True)

SECRET_KEY = env('SECRET_KEY')
if not SECRET_KEY and DEBUG:
    warnings.warn("SECRET_KEY not configured, using a random temporary key.")
    SECRET_KEY = get_random_secret_key()

ALLOWED_HOSTS = env_list('ALLOWED_HOSTS', 'localhost,127.0.0.1')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    # Local apps
    'dhost.builds',
    'dhost.dapps',
    'dhost.github',
    'dhost.ipfs',
    'dhost.users',
    'dhost.oauth2',
    # External apps
    'django_otp',
    'django_otp.plugins.otp_static',
    'django_otp.plugins.otp_totp',
    'oauth2_provider',
    'rest_framework',
    'social_django',
    'storages',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dhost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['dhost/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'dhost.wsgi.application'

DATABASES = {
    'default':
        dj_database_url.config(
            default='sqlite:///db.sqlite3', conn_max_age=600
        )
}

AUTH_USER_MODEL = 'users.User'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
            'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
            'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

CSRF_COOKIE_SECURE = env_bool('CSRF_COOKIE_SECURE', False)
SESSION_COOKIE_SECURE = env_bool('SESSION_COOKIE_SECURE', False)

STATIC_URL = env('STATIC_URL', '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'dhost/static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = env('MEDIA_URL', '/media/')
MEDIA_ROOT = env('MEDIA_ROOT', os.path.join(BASE_DIR, 'media'))

EMAIL_HOST = env('EMAIL_HOST', 'localhost')
EMAIL_PORT = env('EMAIL_PORT', 1025)
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', 'noreply@localhost')
SERVER_EMAIL = env('SERVER_EMAIL', 'root@localhost')

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'account_settings'
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

# REST
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication'
    ],
}

# OAuth2 provider
SCOPES_BACKEND_CLASS = 'oauth2.scopes.SettingsScopes'
OAUTH2_PROVIDER_APPLICATION_MODEL = 'oauth2.Application'
# REFRESH_TOKEN_EXPIRE_SECONDS = env('REFRESH_TOKEN_EXPIRE_SECONDS')

# Social auth
AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_GITHUB_KEY = env('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = env('SOCIAL_AUTH_GITHUB_SECRET')

# AWS S3
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_ACL = env('AWS_DEFAULT_ACL', None)
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env('AWS_S3_REGION_NAME', None)
AWS_S3_CUSTOM_DOMAIN = env('AWS_S3_CUSTOM_DOMAIN', None)
AWS_LOCATION = env('AWS_LOCATION', '')
AWS_MEDIA_BUCKET_NAME = env('AWS_MEDIA_BUCKET_NAME')
AWS_MEDIA_CUSTOM_DOMAIN = env('AWS_MEDIA_CUSTOM_DOMAIN')

if AWS_STORAGE_BUCKET_NAME:
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

if AWS_MEDIA_BUCKET_NAME:
    DEFAULT_FILE_STORAGE = 'dhost.core.storages.S3MediaStorage'

# Redis
REDIS_URL = env('REDIS_URL')
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

# Sentry
SENTRY_DSN = env('SENTRY_DSN')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )

# Debug-toolbar
ENABLE_DEBUG_TOOLBAR = env_bool('ENABLE_DEBUG_TOOLBAR', False)
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    INTERNAL_IPS = env_list('INTERNAL_IPS', '127.0.0.1')

    # To work with Docker
    def show_toolbar(request):
        return True

    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }

# reCAPTCHA
ENABLE_RECAPTCHA = env_bool('ENABLE_RECAPTCHA', False)
if ENABLE_RECAPTCHA:
    INSTALLED_APPS.append('captcha')
    RECAPTCHA_PUBLIC_KEY = env(
        'RECAPTCHA_PUBLIC_KEY', '6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI'
    )
    RECAPTCHA_PRIVATE_KEY = env(
        'RECAPTCHA_PRIVATE_KEY', '6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe'
    )

    if DEBUG:
        # silence the warning about the missing keys
        SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']

    # changing the signup form to use the captcha
    ACCOUNT_FORMS = {
        'signup': 'dhost.users.forms.CaptchaSignupForm',
    }
