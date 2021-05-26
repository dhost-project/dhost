# Demo

For demo purposes a fixture is available, it will load data intot the database so use it for demo on local env only.

The demo fixture is in `dhost/demo/fixture.json`.

To load it run:
```
./manage.py loaddata dhost/demo/fixture.json
```

## Users

This fixture contain users that you can use to connect to the API, or admin site.

### Admin user

Username: `admin`.
Password: `admin`.
Role: `superuser`.

## OAuth2 provider

App `DHost public CLI`, used for the CLI localy.
Client id: `dhost_cli`
Client type: `public`
Authorization grant type: `Resource owner password-based`

App `DHost dashboard`, used for the dashboard localy.
Client id: `dhost_dashboard`
Client secret: `Jqa0e47XoXxPsWVfVMoO2iRCJvfzOtF6lyeuU4hGewpwhwU3LFeOMIA6VT8vMQV8ZVc7nAYVwJgEqOhOf2FWIAsTsZeuIQgZRBZ02La3nesvareMGjicA4aaEJEK7ODN`
Redirect uris: `http://localhost:3000/login/`
Client type: `Confidential`
