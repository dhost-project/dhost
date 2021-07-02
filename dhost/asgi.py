"""ASGI config for dhost project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

from django.core.asgi import get_asgi_application

from dhost import prepare_env

prepare_env()

application = get_asgi_application()
