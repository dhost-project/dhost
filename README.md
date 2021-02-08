# dhost_django


## Setup

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

### Docker
```
# docker-compose up -d
```

Verify
```
# docker-compose ps
```

