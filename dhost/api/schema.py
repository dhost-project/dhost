from rest_framework.schemas import openapi
from rest_framework.schemas.openapi import AutoSchema


class SuperUserSchemaGenerator(openapi.SchemaGenerator):
    def get_schema(self, request=None, public=True):
        schema = super().get_schema(request=request, public=public)
        schema["info"]["termsOfService"] = "https://example.com/tos.html"
        return schema

    def has_view_permissions(self, path, method, view):
        # generate the openapi schema with every views available, by default
        # only authorized views are listed wich can slow down development
        return True


class GroupAutoSchema(AutoSchema):
    def get_tags(self, path, method):
        """Generate the tag from the model name."""
        # by default the tag is generated from the first part of the url wich is
        # a problem in our case because it's always `api`
        # https://www.django-rest-framework.org/api-guide/schemas/#get_tags
        model = getattr(getattr(self.view, "queryset", None), "model", None)
        if model is not None:
            return [model.__name__]
        return ["API"]
