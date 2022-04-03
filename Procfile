release: python manage.py migrate
web: gunicorn dhost.asgi:application -k uvicorn.workers.UvicornWorker -w 4
worker: REMAP_SIGTERM=SIGQUIT celery -A dhost worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery -A dhost beat --loglevel=info
