# Development

To setup you development environment check the `Development` section in the `docs/setup.md` file.

Documentations:
* [Django](https://docs.djangoproject.com/en/3.2/)
* [Django REST](https://www.django-rest-framework.org/)

## Django models

If you change a model you must create a migrations with [makemigrations](https://docs.djangoproject.com/en/3.2/ref/django-admin/#migrate).
```
./manage.py makemigrations
```

And then migrate it you your DB with [migrate](https://docs.djangoproject.com/en/3.2/ref/django-admin/#migrate).
```
./manage.py migrate
```

If you did multiple migrations and you want to squash them you can use:
```
python manage.py squashmigrations
```

More infos [here](https://docs.djangoproject.com/en/3.2/ref/django-admin/#squashmigrations)
