# Tests

There is specific test settings available, this greatly improve speed, to use them simply specify the file when starting them.

```sh
./manage.py test --settings dhost.settings.tests
```

To speed them even more you can also use the `--parallel` flag.

```sh
./manage.py test --settings dhost.settings.tests --parallel
```

Note that in some cases this can fail, for example when testing the `deltestdir` command wich require a folder to be created/deleted.

## Coverage

With the tool coverage we can produce very usefull data wich can help us make to make tests.

To use coverage with django use:

```sh
coverage run manage.py test
```

To see the report use:

```sh
coverage report -m
```

To see the report in HTML format use:

```sh
coverage html
```

More infos [here](https://coverage.readthedocs.io/en/coverage-5.5/#quick-start).

## Test command

The `test` command is modified for this project, the new command can be found in `dhost/core/management/commands/test.py` it's a minor modification witch delete the `TEST_DIR` located in the `.cache` folder (by default at the root of the project).

```sh
./manage.py test
```

The `TEST_DIR` folder contain test datas and can be deleted safely after running a test. You can also delete it manually using the `deltestdir` command.

```sh
./manage.py deltestdir
```

The flag `--noinput` is available for the `deltestdir` command, it will tell Django to not prompt the user for any input, in this case the input is the delete confirmation.

Note that you can also choose to keep the test datas with the `--keepdata` flag when running tests:

```sh
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
