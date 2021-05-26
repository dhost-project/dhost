# Setup

## Docker

The `Dockerfile` file is a great way to start the site with Docker.

## Heroku

The `Procfile` file is a config for [Heroku](https://www.heroku.com/), it define how the app should be started and what commands should be executed before starting it.

This file alone is enought to host the site on Heroku, but there is some extra steps you need to take, main one is setting the environment variables to point to the database. This can be done in the **Settings** tab in your heroku dashboard. Also note that there is a `Heroku Postgres` add-ons available for free [here](https://elements.heroku.com/addons/heroku-postgresql).

## Bare metal

You should check the [Django's deployement guide](https://docs.djangoproject.com/en/3.1/howto/deployment/).

Create the environment.
```
python3.9 -m venv venv
```

Activate it (on linux).
```
source ./venv/bin/activate
```

Install the requirements.
```
pip install -r requirements.txt
```

Migrate the database.
```
./manage.py migrate
```

We will need to compile the translation `.po` files located in the `locale` folder with:
```
./manage.py compilemessages
```

Then you must collect static files with:
```
./manage.py collectstatic
```

This will create a folder containing all the static files raidy to be served by your server.

To serve your static files you can setup a server, or use an AWS S3 bucket, set the permissions to public and collect them there.

Then you will need to create a super user to access the admin page:
```
./manage.py createsuperuser
```

Then you will be able to start the server, for this we will need nginx and we use gunicorn with async support.

## Dev

For developpement you can use a virtual environment.

Create the environment.
```
python3.9 -m venv venv
```

Activate it (on linux).
```
source ./venv/bin/activate
```

Activate it (on windows cmd).
```
.\venv\Script\activate.bat
```

Install the requirements.
```
pip install -r requirements.txt
pip install -r requirements_dev.txt
```

You also use pre-commit git hook to run checks before every commits.
```
pre-commit install
```

Run pre-commit hooks.
```
pre-commit run --all-files
```

Learn more about [pre-commit](https://pre-commit.com/).

Now every time you commit the checks will run `yapf`, `flake8` and other usefull tools to format the code.

You can and should test the code, you can do so with:
```
./manage.py test
```

You should also check the `coverage` package wich generate a report about the tests coverage of the app, use it with:
```
coverage run manage.py test
```

To see the report use:
```
coverage report -m
```

To see the report in HTML format use:
```
coverage html
```

There is also an editorconfig file (`.editorconfig`) that can be used with your IDE or text editor, more infos [here](https://editorconfig.org/).

More infos in the `docs/test.md` file.

If you change a model you must create a migrations:
```
./manage.py makemigrations
```

And then migrate it you your DB with:
```
./manage.py migrate
```

### Commands

The list of commands can be found in the `docs/commands.md` file.

## Config

The Django config is defined in the `dhost/settings.py` file, and are set with environment variables mainly.

### Environment variables

The environment variables allow us to define the application settings without having to edit the `settings.py` file. On linux you can use `export ENV_NAME=VAR_VALUE` to set one.

The list of variables there default values and descriptions can be found in the `docs/environment_variables.md` file.

### AWS

The AWS environment variables can be found in the `docs/aws_setup.md` file.
