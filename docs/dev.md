# Development

To setup you development environment check the `Development` section in the `docs/setup.md` file.

Documentations:

* [Django](https://docs.djangoproject.com/en/3.2/)
* [Django REST](https://www.django-rest-framework.org/)

## Django models

If you change a model you must create a migrations with [makemigrations](https://docs.djangoproject.com/en/3.2/ref/django-admin/#migrate).

```sh
./manage.py makemigrations
```

And then migrate it you your DB with [migrate](https://docs.djangoproject.com/en/3.2/ref/django-admin/#migrate).

```sh
./manage.py migrate
```

If you did multiple migrations and you want to squash them you can use:

```sh
python manage.py squashmigrations
```

More infos [here](https://docs.djangoproject.com/en/3.2/ref/django-admin/#squashmigrations)

## Dependencies

The `requirements.txt` and `requirements_dev.txt` contains the list of packages used for this project.

To install dependencies use `pip`.

```sh
pip install -r requirements.txt
```

If you add a package run `sort-requirements` to order the list.

```sh
sort-requirements requirements.txt
```

You can also run `pre-commit` to re-order the requirements.

```sh
pre-commit run --all-file
```

You can upgrade packages with `pip-upgrader`.

```sh
pip-upgrade
```

Make sure tests are still passing.
