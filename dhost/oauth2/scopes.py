from oauth2_provider.scopes import BaseScopes


class SettingsScopes(BaseScopes):
    def get_all_scopes(self):
        return {
            "read": "Full read scope",
            "write": "Full write scope",
            "delete": "Full delete scope",
            "user": "User read write scope",
            "user:read": "User read scope",
            "user:email": "User email read scope",
        }

    def get_available_scopes(
        self, application=None, request=None, *args, **kwargs
    ):
        return ["read", "write", "delete", "user", "user:read", "user:email"]

    def get_default_scopes(
        self, application=None, request=None, *args, **kwargs
    ):
        return ["user:read"]
