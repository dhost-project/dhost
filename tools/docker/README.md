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
* [API and OAuth server](http://localhost:8000/api/) on port: `8000`
* [Grafana](http://localhost:3030/) on port: `3030`
* [Prometheus](http://localhost:9090/) on port: `9090`
* [Task Monitor (Flower)](http://localhost:5555/) on port: `5555`
* [Mail interface (Mailhog)](http://localhost:8025/) on port: `8025`
* [DB explorer (Adminer)](http://localhost:8080/) on port: `8080`
* Database (PostgreSQL) on port: `5432`
* Message Broker (Redis) on port: `6379`

You can also use the CLI to communicate with the API.
