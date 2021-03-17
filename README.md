# dhost_django

## Setup

### Docker

You can use Docker for dev or production:

```
# docker build . -t 'api'
```

```
# docker run api
```

You should be able to visit it at: [http://localhost:8000/](http://localhost:8000/).

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

Create superuser:
```
python manage.py createsuperuser
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

Some configurations use environment variables, the list can be found [here](docs/environment_variables.md).

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

## Techs

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
- isort
- pre-commit config
