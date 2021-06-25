# Auth OAuth2 provider and OAuth2 clients API routes

The package [django-oauth-toolkit](https://django-oauth-toolkit.readthedocs.io/en/latest/) is used for the project.

## OAuth2 Authorization code flow

The OAuth2 flow used for the dashboard web client.

To create an app go to the admin interface : `http://localhost:8000/admin/oauth2/application/add/`.

If you have a front-end with JS app, you should create an app with the following options:

* Client Type: confidential
* Authorization Grant Type: Authorization code
* Redirect uris: _your front-end app uri_ (example: `http://localhost:3000/login/`)

Note that if the app is a first-party you can also check the `Skip authorization` box to skip the `Authorize <app>?` page.

Store the `client_id` and `client_secret` in the back-end and ONLY the back-end of you app.

To start the authorization flow redirect the user to the URL:

```none
http://localhost:8000/oauth2/authorize/?response_type=code&client_id=<client_id>&redirect_uri=<front_end_app_uri>
```

* `client_id` is the app id we got earlier from the admin page
* `redirect_uri` must be the same has passed in the app creation otherwise it won't work

If the user decide to Authorize the app he will be redirected to the URI with a parameter:

```none
<front_end_app_uri>?code=<code>
```

You need to grab this code and send a request from the BACKEND of your app because we'll send a secret:

```shell
curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://localhost:8000/oauth2/token/" -d "client_id=<client_id>" -d "client_secret=<client_secret>" -d "code=<code>" -d "redirect_uri=<front_end_app_uri>" -d "grant_type=authorization_code"
```

Note that you only have a short time to get the token.

The OAuth2 provider will return an `access_token` and `refresh_token` back to the BACKEND server in this format:

```json
{
    "access_token": "<access_token>",
    "token_type": "Bearer",
    "expires_in": 36000,
    "refresh_token": "<refresh_token>",
    "scope": "read write groups"
}
```

At this point you can send the user his `access_token` so he will be able to make call to the REST database, or you can decide on another flow where the backend server act like a proxy, making the requests to it wich will then be sent to the API server with the `access_token`. This method slows down the traffic because each requests take twice has long (because they are bounced).

To use the token place it in the headers

Grab the `access_token` and use it in requests's headers like so:

```shell
curl -H "Authorization: Bearer <access_token>" http://localhost:8000/<api_route>
```

When the token is close to expiration the backend server can refresh it by making a request to the authorization server.

To refresh the `access_token` use the following request:

```shell
curl -X POST -d "grant_type=refresh_token&refresh_token=<refresh_token>&client_id=<client_id>&client_secret=<your_client_secret>" http://localhost:8000/oauth2/token/
```

To learn more about OAuth2 visit:

* `https://www.oauth.com/`
* `https://aaronparecki.com/oauth-2-simplified/`

## OAuth2 ROPC

The OAuth2 flow used for the CLI app.

* Client id: `test` (just for this example)
* Client Type: public
* Authorization Grant Type: Resource owner password-based
* Redirect uris: `Empty`

With the user credentials the CLI will be able to call:

```shell
curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://localhost:8000/oauth2/token/" -d "client_id=test" -d "username=admin" -d "password=admin" -d "grant_type=password"
```
