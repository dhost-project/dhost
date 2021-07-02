"""WSGI config for dhost project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application

from dhost import prepare_env

prepare_env()

application = get_wsgi_application()
