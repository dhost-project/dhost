# dhost_django

Techs:
- Django
- Docker
- Sentry
- Github CI
- Heroku
- Gunicorn
- PostgreSQL
- Adminer
- Mailhog

### Docker

```
# docker-compose build
```

```
# docker-compose up -d
```

Verify
```
# docker-compose ps
```

## Manual Setup

Python virtual environment
```
python3.8 -m venv venv
```

Activate virtual environment
```
source venv/bin/activate
```

Install python libs
```
pip install -r requirements.txt
```

Create database:
```
python manage.py migrate
```

Launch server:
```
python manage.py runserver
```

## Dev

When changing models:
```
python manage.py makemigrations
```

## Environment variables

Some configuration use the env var, the following are used:
```
DEBUG=[True/False]
ALLOWED_HOSTS=[127.0.0.1,localhost]
SECRET_KEY=[auto_generated for dev only]
SENTRY_DSN=[sentry_dsn_url]
```

