# Tests

The `test` command is modified for this project, the new command can be found in `dhost/core/management/commands/test.py` it's a minor modification witch delete the `TEST_DIR` located in the `.cache` folder (by default at the root of the project).

```
python manage.py test
```

The `TEST_DIR` folder contain test datas and can be deleted safely after running a test. You can also delete it manually using the `deltestdir` command.

```
python manage.py deltestdir
```

The flag `--noinput` is available for the `deltestdir` command, it will tell Django to not prompt the user for any input, in this case the input is the delete confirmation.

Note that you can also choose to keep the test datas with the `--keepdata` flag when running tests:

```
python manage.py test --keepdata
```

The `test` command is modified to allow the testing of user models wich generate an avatar that is stored in the `MEDIA_ROOT` wich should be modified. The `TEST_DIR` can be modified in the settings or in env variables of the same name.

To use the custom `MEDIA_ROOT` in your test use the `override_settings`:

```
from django.conf import settings
from django.test import TestCase, override_settings

@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class ExampleTestCase(TestCase):
    [...]
```
