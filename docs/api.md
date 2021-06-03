# API

## OpenAPI Schema

An OpenAPI Schema is available in the doc at `docs/openapi-schema.yml`. You can view it in your browser with the [Swagger Editor](https://editor.swagger.io/).

## Update the schema

To update the schema you can use the `generateschema` command from Django REST framework.
```
./manage.py generateschema --file docs/openapi-schema.yml
```
