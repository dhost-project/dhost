# dhost_django

Techs:
- Django
- REST
- Docker
- Sentry
- Github CI
- Heroku
- Gunicorn
- PostgreSQL
- Yapf

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
DEBUG_TOOLBAR=[True/False]
ALLOWED_HOSTS=[127.0.0.1,localhost]
SECRET_KEY=[auto_generated for dev only]
SENTRY_DSN=[sentry_dsn_url]
```

## Style

Black is used has a code formater, you can run it with `black .`, the file `pyproject.toml` configure Black.

There is also an editorconfig file (`.editorconfig`) that can be used with your IDE or text editor, more infos [here](https://editorconfig.org/).

To use flake8 try:
```
flake8 dhost --max-line-length 119 --per-file-ignores="__init__.py:F401" --extend-exclude "**/migrations/*"
```
