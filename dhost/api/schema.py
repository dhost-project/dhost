from rest_framework.schemas import openapi


class SuperUserSchemaGenerator(openapi.SchemaGenerator):

    def has_view_permissions(self, path, method, view):
        # generate the openapi schema with every views available, by default
        # only authorized views are listed wich can slow down development
        return True
