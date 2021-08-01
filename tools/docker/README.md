# Docker

## Requirements

- Docker
- Docker compose

## Setup

To start the project.

```shell
docker-compose up -d --build
```

Apply migrations.

```shell
docker-compose run --rm api python manage.py migrate
```

Load fixture (demo data).

```shell
docker-compose run --rm api python manage.py loaddata dhost/demo/fixture.json
```

Collect static files.

```shell
docker-compose run --rm api python manage.py collectstatic
```

Verify.

```shell
docker-compose ps
```

When you want to stop it.

```shell
docker-compose down
```

Visit:

* [Dahsboard](http://localhost:3000/) on port: `3000`
* [API and OAuth server](http://127.0.0.1:8000/) on port: `8000`
* [Mailhog](http://localhost:8025/) on port: `8025`
* [Adminer](http://localhost:8080/) on port: `8080`
* PostgreSQL on port: `5432`
* Redis on port: `6379`

You can also use the CLI to communicate with the API.

## Light dev

There is a light version of the docker-compose file available.

```shell
docker-compose -f docker-compose_light.yml up -d --build
```
