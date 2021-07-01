# API

## OpenAPI Schema

An OpenAPI Schema is available in the doc at `docs/openapi-schema.yml`. You can view it in your browser with the [Swagger Editor](https://editor.swagger.io/).

The [http://localhost:8000/openapi](http://localhost:8000/openapi) page send the schema, it can be viewed with [Redoc](https://github.com/Redocly/redoc) at [http://localhost:8000/redoc/](http://localhost:8000/redoc/).

You are seeing only the available routes, when you are not connected you don't have access to any, to do so either go to the `/admin` page or the browsable API `/api/v1/` and login, then go back to the `/redoc` page.

## Update the schema

To update the schema you can use the `generateschema` command from Django REST framework.

```sh
./manage.py generateschema --file docs/openapi-schema.yml
```
