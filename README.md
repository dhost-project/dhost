# dhost_django

Techs:
    - Django
    - Docker
    - Sentry
    - Travis CI
    - Heroku
    - Gunicorn

### Docker
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

## Prod and dev

Create super user:
```
python manage.py createsuperuser
```

create API token:
```
python manage.py drf_create_token <username>
```

In case of problem with pip installation:
```
sudo apt install libpq-dev python-dev
```

## Environment variables

Some configuration use the env var, the following are used:
```
DEBUG=[True/False]
ALLOWED_HOSTS=[127.0.0.1,localhost]
SECRET_KEY=[auto_generated for dev only]
SENTRY_DSN=[sentry_dsn_url]
```

## Styling guide

To check the style install flake8 (in requirements_dev) and run:
```
flake8 dhost --max-line-length 119 --per-file-ignores="__init__.py:F401" --ignore W391
```

