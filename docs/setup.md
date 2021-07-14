# Setup

## Environment variables

The environment variables allow us to define the application settings without having to edit the settings. On linux you can use `export ENV_NAME=VAR_VALUE` to set one.

The list of variables there default values and descriptions can be found in [environment_variables.md](./environment_variables.md).

### AWS S3

AWS can be used for static and media storage inside an S3 bucket. The AWS environment variables can be found in [aws.md](./aws.md).

## Heroku

[Procfile](./../Procfile) is a config file for [Heroku](https://www.heroku.com/), it define how the app should be started and what commands should be executed before starting it.

This file alone is enought to host the site on Heroku, but there is some extra steps you need to take, main one is setting the environment variables to point to the database. This can be done in the **Settings** tab in your heroku dashboard. Also note that there is a `Heroku Postgres` add-ons available for free [here](https://elements.heroku.com/addons/heroku-postgresql).

You should check [environment_variables.md](./environment_variables.md) for more informations about variables.

## Bare metal

You should check the [Django's deployement guide](https://docs.djangoproject.com/en/3.1/howto/deployment/).

Create the environment.

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
```

At this point you should check [environment_variables.md](./environment_variables.md) for more informations about variables.

Mainly `DJANGO_ENV`, `SECRET_KEY` and `DATABASE_URL`.

Migrate the database.

```bash
./manage.py migrate
```

Then you need to collect static files.

```bash
./manage.py collectstatic
```

This will create a folder containing all the static files raidy to be served by your server.

To serve your static files you can setup a server, use an AWS S3 bucket, or use a Google Cloud bucket.

Then you will need to create a super user to access the admin panel.

```bash
./manage.py createsuperuser
```

Then you will be able to start the server, for this we will need nginx and we use gunicorn with async support.
