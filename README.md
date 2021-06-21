# DHost API

## Setup

For a complete setup guide go to [docs/setup.md](docs/setup.md) or use Docker:

```
docker build . -t 'api' -f Dockerfile_dev
```

```
docker run -p 8000:8000 api
```

Visit the browsable API: [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).

Login with `admin` `admin` to make requests.
