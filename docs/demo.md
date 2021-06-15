# Demo

For demo purposes a fixture is available, it will load data intot the database so use it for demo on local env only.

The demo fixture is in `dhost/demo/fixture.json`.

## Load fixture

```
./manage.py loaddata dhost/demo/fixture.json
```

For more infos check out the `Demo` in the `docs/setup.md` file.

## Fixture content

### Users

This fixture contain users that you can use to connect to the API, or admin site.

| Username | Password | Role | Mail | CLI token |
| --- | --- | --- | --- | --- |
| `admin` | `admin` | `superuser` | `admin@example.com` | `admintoken` |
| `userone` | `vW5yhEsNhQeQhm2gFf` | | `userone@example.com` | `uonetoken` |
| `usertwo` | `pVD2tvtaxAWpsqeXEc` | | `usertwo@example.com` | `utwotoken` |

### OAuth2 provider

| App | `DHost public CLI` |
| --- | --- |
| Client id | `dhost_cli` |
| Client type | `public` |
| Grant type | `Resource owner password-based` |

| App | `DHost dashboard` |
| --- | --- |
| Client id | `dhost_dashboard` |
| Client secret | `Jqa0e47XoXxPsWVfVMoO2iRCJvfzOtF6l` |
| Redirect uris | `http://localhost:3000/login/` |
| Client type | `Confidential` |
| Grant type | `Authorization code` |
| Skip authorization | `True` |

## Update the fixture

To update the fixture you should first load it (or not if you want to completly modify it), then edit the data.

And then dump it back into the folder.
```
./manage.py dumpdata > dhost/demo/fixture.json
```

Don't forget to reformat it.
