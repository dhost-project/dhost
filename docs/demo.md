# Demo

For demo purposes a fixture is available, it will load data intot the database so use it for demo on local env only.

The demo fixture is in `dhost/demo/fixture.json`.

Load fixture.
```
./manage.py loaddata dhost/demo/fixture.json
```

For more infos check out the `Demo` in the `docs/setup.md` file.

## Users

This fixture contain users that you can use to connect to the API, or admin site.

| Username | Password | Role |
| --- | --- | --- |
| `admin` | `admin` | `superuser` |
| `userone` | `vW5yhEsNhQeQhm2gFf` | |
| `usertwo` | `pVD2tvtaxAWpsqeXEc` | |

## OAuth2 provider

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
