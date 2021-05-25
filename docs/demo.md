# Demo

For demo purposes a fixture is available, it will load data intot the database so use it for demo on local env only.

The demo fixture is in `dhost/demo/fixture.json`.

To load it run:
```
./manage.py loaddata ./dhost/demo/fixture.json
```

## Users

This fixture contain users that you can use to connect to the API, or admin site.

### Admin user

Username: `admin`.
Password: `admin`.
Role: `superuser`.
