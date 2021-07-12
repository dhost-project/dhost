# API

## OpenAPI Schema

An OpenAPI Schema is available in the doc at [docs/openapi-schema.yml](https://github.com/dhost-project/dhost/blob/master/docs/openapi-schema.yml). You can view it in your browser with the [Swagger Editor](https://editor.swagger.io/).

The [localhost:8000/api/openapi](http://localhost:8000/api/openapi) page send the schema, it can be viewed with [Redoc](https://github.com/Redocly/redoc) at [localhost:8000/api/redoc/](http://localhost:8000/api/redoc/).

You are only seeing available routes, when you are not connected you don't have access to any, to do so either go to the [localhost:8000/admin/login/](http://localhost:8000/admin/login/) page or the browsable API [localhost:8000/api-auth/login/](http://localhost:8000/api-auth/login/?next=/api/) and login, then go back to the [/api/redoc](http://localhost:8000/api/redoc/) page.

## Update the schema

To update the schema you can use the [generateschema](https://www.django-rest-framework.org/coreapi/schemas/#generating-a-schema-with-the-generateschema-management-command) command from Django REST framework.

```sh
./manage.py generateschema --file docs/openapi-schema.yml
```
