import os

import dj_database_url

from dhost.utils import get_version
from dhost.utils.env import env, env_bool, env_float, env_int, env_list

# dhost folder (apps dir)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# git root
ROOT_DIR = os.path.dirname(BASE_DIR)

SITE_ID = env_int("SITE_ID", 1)

ALLOWED_HOSTS = env_list("ALLOWED_HOSTS", "localhost,127.0.0.1")

INTERNAL_IPS = env_list("INTERNAL_IPS", "127.0.0.1")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    # Local apps
    "dhost.api",
    "dhost.builds",
    "dhost.core",
    "dhost.dapps",
    "dhost.frontend",
    "dhost.github",
    "dhost.ipfs",
    "dhost.logs",
    "dhost.notifications",
    "dhost.users",
    "dhost.oauth2",
    # External apps
    "django_otp",
    "django_otp.plugins.otp_static",
    "django_otp.plugins.otp_totp",
    "oauth2_provider",
    "rest_framework",
    "social_django",
    "storages",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "oauth2_provider.middleware.OAuth2TokenMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_otp.middleware.OTPMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "crum.CurrentRequestUserMiddleware",
]

ROOT_URLCONF = "dhost.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "frontend", "build")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "dhost.wsgi.application"

DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3", conn_max_age=600
    )
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

REDIS_URL = env("REDIS_URL")

if REDIS_URL:
    CACHES.update(
        {
            "redis": {
                "BACKEND": "django_redis.cache.RedisCache",
                "LOCATION": REDIS_URL,
                "OPTIONS": {
                    "CLIENT_CLASS": "django_redis.client.DefaultClient",
                    "IGNORE_EXCEPTIONS": True,
                },
            }
        }
    )

    SESSION_ENGINE = "django.contrib.sessions.backends.cache"

    SESSION_CACHE_ALIAS = "redis"

AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation."
        "NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(os.path.dirname(ROOT_DIR), "locale"),)

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "frontend", "build", "static")]

MEDIA_URL = "/media/"

MEDIA_ROOT = env("MEDIA_ROOT", os.path.join(ROOT_DIR, "media"))

FIXTURE_DIRS = [os.path.join(ROOT_DIR, "tools", "fixtures")]

EMAIL_HOST = env("EMAIL_HOST", "localhost")

EMAIL_PORT = env("EMAIL_PORT", 1025)

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", "noreply@localhost")

SERVER_EMAIL = env("SERVER_EMAIL", "root@localhost")

# auth
LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "account_settings"

LOGOUT_URL = "logout"

LOGOUT_REDIRECT_URL = "login"

# REST
# https://www.django-rest-framework.org/
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication"
    ],
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.AcceptHeaderVersioning",
    "DEFAULT_VERSION": "1.0",
    "ALLOWED_VERSIONS": ("1.0",),
    "DEFAULT_SCHEMA_CLASS": "dhost.api.schema.GroupAutoSchema",
}

# OAuth2 provider
# https://django-oauth-toolkit.readthedocs.io/en/latest/
SCOPES_BACKEND_CLASS = "oauth2.scopes.SettingsScopes"

OAUTH2_PROVIDER_APPLICATION_MODEL = "oauth2.OAuth2Application"

# REFRESH_TOKEN_EXPIRE_SECONDS = env('REFRESH_TOKEN_EXPIRE_SECONDS')

AUTHENTICATION_BACKENDS = (
    "oauth2_provider.backends.OAuth2Backend",
    "django.contrib.auth.backends.ModelBackend",
    "social_core.backends.github.GithubOAuth2",
)

# Social auth
# https://python-social-auth.readthedocs.io/en/latest/
SOCIAL_AUTH_GITHUB_KEY = env("SOCIAL_AUTH_GITHUB_KEY")

SOCIAL_AUTH_GITHUB_SECRET = env("SOCIAL_AUTH_GITHUB_SECRET")

SOCIAL_AUTH_GITHUB_SCOPE = [
    # 'repo',
    # 'repo_deployment',
    # 'read:repo_hook',
    # 'user:email',
]

GITHUB_REPOS_ROOT = env("GITHUB_REPOS_ROOT", os.path.join(MEDIA_ROOT, "github"))

# Celery
CELERY_BROKER_URL = env("CELERY_BROKER_URL", "redis://localhost:6379/0")

CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

CELERY_TASK_TRACK_STARTED = True

CELERY_TASK_TIME_LIMIT = env_int("CELERY_TASK_TIME_LIMIT", 1800)

CELERY_TASK_SOFT_TIME_LIMIT = env_int("CELERY_TASK_SOFT_TIME_LIMIT", 1700)

GITHUB_REPOS_ROOT = env("GITHUB_REPOS_ROOT", os.path.join(MEDIA_ROOT, "github"))

# IPFS
IPFS_HTTP_API_URL = env("IPFS_HTTP_API_URL", "http://127.0.0.1:5001/api/")
IPFS_CLUSTER_API_URL = env("IPFS_CLUSTER_API_URL", "https://cluster0:9094/")


# putting the `TEST_DIR` inside the `.cache` folder protect from loosing data
# that musn't be deleted
TEST_DIR = os.path.join(env("TEST_DIR", ".cache"), ".test_dir")

TEST_MEDIA_ROOT = env("TEST_MEDIA_ROOT", os.path.join(TEST_DIR, "media"))

LOG_ROOT = env("LOG_ROOT", ROOT_DIR)

LOG_LEVEL = env("LOG_LEVEL", "INFO")

# https://docs.djangoproject.com/en/dev/topics/logging/#configuring-logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "django.server": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "django.server": {
            "class": "logging.StreamHandler",
            "formatter": "django.server",
        },
        "mail_admins": {
            "class": "django.utils.log.AdminEmailHandler",
        },
        "github_api": {
            "class": "logging.FileHandler",
            "filename": os.path.join(LOG_ROOT, "github_api.log"),
            "formatter": "django.server",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": LOG_LEVEL,
        },
        "django.server": {
            "handlers": ["django.server"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        "dhost.github.github_api": {
            "handlers": ["console", "github_api"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}

# Sentry
# https://docs.sentry.io/platforms/python/guides/django/
SENTRY_DSN = env("SENTRY_DSN")

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.celery import CeleryIntegration
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            DjangoIntegration(),
            CeleryIntegration(),
        ],
        traces_sample_rate=env_float("SENTRY_TRACES_SAMPLE_RATE", 1.0),
        send_default_pii=env_bool("SENTRY_SEND_DEFAULT_PII", True),
        release=get_version(),
    )
