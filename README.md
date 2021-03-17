# dhost_django

Techs:
- Django
- REST
- Docker
- Sentry
- Heroku
- Gunicorn
- PostgreSQL

Dev:
- Github CI
- Yapf
- Editorconfig

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
```

## Style

Yapf is used has a code formater, you can run it with `yapf -r -i dhost`.

There is also an editorconfig file (`.editorconfig`) that can be used with your IDE or text editor, more infos [here](https://editorconfig.org/).

Flake8 is used has linter for code quality, to use it run:
```
flake8 dhost
```

There is also a pre-commit hooks, simply commit or use:

Install it with:
```
pre-commit install
```

And run it with:
```
pre-commit run --all-files
```

Learn more about it [here](https://pre-commit.com/)
