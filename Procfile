release: python manage.py migrate
web: gunicorn dhost.asgi:application --workers 4 --worker-class uvicorn.workers.UvicornWorker
