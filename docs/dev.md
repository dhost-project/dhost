# Development

## Local environment

Create a Python virtual environment.

```bash
python3.9 -m venv venv
```

Activate it (on linux).

```bash
source ./venv/bin/activate
```

Install the requirements.

```bash
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

On Windows there is a specific requirements file in `tools/requirements_windows.txt`.

Collect static files.

```bash
./manage.py collectstatic
```

Migrate the database.

```bash
./manage.py migrate
```

You can now run the development server. Next time you want to start the server, this is the only command you will need (after activating your virtual environment).

```bash
./manage.py runserver
```

Additionnaly you can [load a fixture](https://docs.djangoproject.com/en/dev/ref/django-admin/#loaddata) located in [dhost/demo/fixture.json](./../dhost/demo/fixture.json). More informations in [dhost/demo/README.md](./../dhost/demo/README.md).

```bash
./manage.py loaddata dhost/demo/fixture.json
```

If you don't want to load the data in the database but still want to use the fixture, you can use the [testserver](https://docs.djangoproject.com/en/dev/ref/django-admin/#testserver).

```bash
./manage.py testserver dhost/demo/fixture.json
```

## Tests

There is specific test settings available, this greatly improve speed, to use them simply specify the file when starting them.

```bash
./manage.py test --settings dhost.settings.tests
```

Note that the `test` command is modified for this project, the new command can be found in [dhost/core/management/commands/test.py](./../dhost/core/management/commands/test.py), it's a minor modification witch delete the `TEST_DIR` located in the `.cache` folder (by default at the root of the project).

The `TEST_DIR` folder contain test datas and can be deleted safely after running a test. You can also delete it manually using the `deltestdir` command.

```bash
./manage.py deltestdir
```

The flag `--noinput` is available for the `deltestdir` command, it will tell Django to not prompt the user for any input, in this case the input is the delete confirmation.

Note that you can also choose to keep the test datas with the `--keepdata` flag when running tests:

```bash
./manage.py test --keepdata
```

The `test` command is modified to allow the testing of user models wich generate an avatar that is stored in the `MEDIA_ROOT` wich should be modified. The `TEST_DIR` can be modified in the settings or in env variables of the same name.

To use the custom `MEDIA_ROOT` in your test use the `override_settings`:

```python
from django.conf import settings
from django.test import TestCase, override_settings

@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class ExampleTestCase(TestCase):
   [...]
```

### Coverage

To use [coverage](https://coverage.readthedocs.io/en/coverage-5.5/#quick-start) with django use:

```bash
coverage run manage.py test
```

To see the report use:

```bash
coverage report -m
```

To see the report in HTML format use:

```bash
coverage html
```

## Links

* [Django doc](https://docs.djangoproject.com/en/3.2/)
* [Django REST doc](https://www.django-rest-framework.org/)
