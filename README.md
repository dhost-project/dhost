# DHost

![infra](docs/dhost_infra.png)

## Setup

For a complete setup guide go to [docs/setup.md](./docs/setup.md) or use Docker [tools/docker/README.md](./tools/docker/README.md).

```ssh
cd tools/docker
```

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

Visit the site: [http://localhost:8000/](http://localhost:8000/).

Login with `admin` `admin` to make requests.

## Contributing

To start contributing please refer to the [CONTRIBUTING.md](./CONTRIBUTING.md) doc.

## License

The project is licensed under the [MIT License](./LICENSE).
