# Setup

## Environment variables

The environment variables allow us to define the application settings without having to edit the settings. On linux you can use `export ENV_NAME=VAR_VALUE` to set one.

The list of variables there default values and descriptions can be found in the [docs/environment_variables.md](https://github.com/dhost-project/dhost/blob/master/docs/environment_variables.md) file.

### AWS

AWS can be used for static and media storage inside a bucket.
The AWS environment variables can be found in the [docs/aws_setup.md](https://github.com/dhost-project/dhost/blob/master/docs/aws_setup.md) file.

## Heroku

The `Procfile` file is a config for [Heroku](https://www.heroku.com/), it define how the app should be started and what commands should be executed before starting it.

This file alone is enought to host the site on Heroku, but there is some extra steps you need to take, main one is setting the environment variables to point to the database. This can be done in the **Settings** tab in your heroku dashboard. Also note that there is a `Heroku Postgres` add-ons available for free [here](https://elements.heroku.com/addons/heroku-postgresql).

You should check the [docs/environment_variables.md](https://github.com/dhost-project/dhost/blob/master/docs/environment_variables.md) file for more informations about variables.

## Bare metal

You should check the [Django's deployement guide](https://docs.djangoproject.com/en/3.1/howto/deployment/).

Create the environment.

```sh
python3.9 -m venv venv
```

Activate it (on linux).

```sh
source ./venv/bin/activate
```

Install the requirements.

```sh
pip install -r requirements.txt
```

At this point you should check the [docs/environment_variables.md](https://github.com/dhost-project/dhost/blob/master/docs/environment_variables.md) file for more informations about variables.
Mainly `DEBUG`, `SECRET_KEY` and `DATABASE_URL`.

Migrate the database.

```sh
./manage.py migrate
```

Then you must collect static files with:

```sh
./manage.py collectstatic
```

This will create a folder containing all the static files raidy to be served by your server.

To serve your static files you can setup a server, or use an AWS S3 bucket, set the permissions to public and collect them there.

Then you will need to create a super user to access the admin page:

```sh
./manage.py createsuperuser
```

Then you will be able to start the server, for this we will need nginx and we use gunicorn with async support.
