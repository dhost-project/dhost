from django.contrib.contenttypes.models import ContentType

from .models import APILog, ActionFlags

# the list of name of inherited `Dapp` models
DAPP_MODELS_LIST = ['ipfsdapp']
ENV_VAR_MODEL_LIST = ['envvar']
BUNDLE_MODELS_LIST = ['bundle']
BUILD_OPTIONS_MODEL_LIST = ['buildoptions']
GITHUB_OPTIONS_MODEL_LIST = ['githuboptions']


class APILogViewSetMixin:
    """Add the ability to log actions, logged actions are on state changing
    calls from viewsets (create, update, partial_update, destroy).
    """

    # log_on_<action> define if we should log the specific action, this allow
    # a specific configuration for the view set using theis mixin
    log_on_create = True
    # <action>_action_flag define wich flag to use for the action, if not set
    # the get_<action>_action_flag will try to guess wich flag to use based on
    # a pre-determined list of options
    # the action flag must be an element from the class `ActionFlags`
    create_action_flag = None
    log_on_update = True
    update_action_flag = None
    log_on_partial_update = True
    partial_update_action_flag = None
    log_on_destroy = True
    destroy_action_flag = None

    def get_create_action_flag(self, obj=None):
        """Get the create flag.

        Will return the action flag to use during an object creation.
        Either get the action flag form the class var `create_action_flag` or
        try to guess it based on the current object model wich is gathered from
        the `get_obj_model` function.

        Returns:
            ActionFlags: the appropriate action flag
        """
        if self.create_action_flag:
            return self.create_action_flag
        if obj:
            obj_model = self.get_obj_model(obj).model
            if obj_model in DAPP_MODELS_LIST:
                return ActionFlags.DAPP_ADDITION
            elif obj_model in ENV_VAR_MODEL_LIST:
                return ActionFlags.ENV_VAR_ADDITION
            elif obj_model in BUILD_OPTIONS_MODEL_LIST:
                return ActionFlags.BUILD_OPTIONS_ADDITION
            elif obj_model in GITHUB_OPTIONS_MODEL_LIST:
                return ActionFlags.GITHUB_OPTIONS_ADDITION
            elif obj_model in BUNDLE_MODELS_LIST:
                return ActionFlags.BUNDLE_ADDITION
        raise Exception('Please provide a `create_action_flag`.')

    def perform_create(self, serializer):
        # we need the object to create the log, and the simplest way to get it
        # is during the creation, we then set the value of `sel.obj` to the obj
        self.obj = serializer.save()

    def create(self, request, *args, **kwargs):
        """Log the action on a create call."""
        response = super().create(request, *args, **kwargs)
        if self.log_on_create:
            obj = self.obj
            action_flag = self.get_create_action_flag(obj)
            self.log_action(request, obj=obj, action_flag=action_flag)
        return response

    def get_update_action_flag(self):
        """Get the update flag.

        Will return the action flag to use during an object update.
        Either get the action flag form the class var `update_action_flag` or
        try to guess it based on the current object model wich is gathered from
        the `get_obj_model` function.

        Returns:
            ActionFlags: the appropriate action flag
        """
        if self.update_action_flag:
            return self.update_action_flag
        obj_model = self.get_obj_model(self.get_object()).model
        if obj_model in DAPP_MODELS_LIST:
            return ActionFlags.DAPP_CHANGE
        elif obj_model in ENV_VAR_MODEL_LIST:
            return ActionFlags.ENV_VAR_CHANGE
        elif obj_model in BUILD_OPTIONS_MODEL_LIST:
            return ActionFlags.BUILD_OPTIONS_CHANGE
        elif obj_model in GITHUB_OPTIONS_MODEL_LIST:
            return ActionFlags.GITHUB_OPTIONS_CHANGE
        raise Exception('Please provide an `update_action_flag`.')

    def update(self, request, *args, **kwargs):
        """Log the action on an update call."""
        response = super().update(request, *args, **kwargs)
        if self.log_on_update:
            self.log_action(request,
                            obj=self.get_object(),
                            action_flag=self.get_update_action_flag())
        return response

    def get_partial_update_action_flag(self):
        """Get the partial update flag.

        Will return the action flag to use during an object partial update.
        Either get the action flag form the class var
        `partial_update_action_flag` or try to guess it based on the current
        object model wich is gathered from the `get_obj_model` function.

        Returns:
            ActionFlags: the appropriate action flag
        """
        if self.partial_update_action_flag:
            return self.partial_update_action_flag
        try:
            return self.get_update_action_flag()
        except Exception:
            raise Exception('Please provide a `partial_update_action_flag` or '
                            '`update_action_flag`.')

    def partial_update(self, request, *args, **kwargs):
        """Log the action on an partial update call."""
        response = super().partial_update(request, *args, **kwargs)
        if self.log_on_partial_update:
            self.log_action(request,
                            obj=self.get_object(),
                            action_flag=self.get_partial_update_action_flag())
        return response

    def get_destroy_action_flag(self):
        """Get the destroy flag.

        Will return the action flag to use during an object partial update.
        Either get the action flag form the class var `destroy_action_flag` or
        try to guess it based on the current object model wich is gathered from
        the `get_obj_model` function.

        Returns:
            ActionFlags: the appropriate action flag
        """
        if self.destroy_action_flag:
            return self.destroy_action_flag
        obj_model = self.get_obj_model(self.get_object()).model
        if obj_model in ENV_VAR_MODEL_LIST:
            return ActionFlags.ENV_VAR_DELETION
        elif obj_model in BUILD_OPTIONS_MODEL_LIST:
            return ActionFlags.BUILD_OPTIONS_DELETION
        elif obj_model in GITHUB_OPTIONS_MODEL_LIST:
            return ActionFlags.GITHUB_OPTIONS_DELETION
        elif obj_model in BUNDLE_MODELS_LIST:
            return ActionFlags.BUNDLE_DELETION
        raise Exception('Please provide a `destroy_action_flag`.')

    def destroy(self, request, *args, **kwargs):
        """Log the action on a delete call."""
        response = super().destroy(request, *args, **kwargs)
        if self.log_on_destroy:
            self.log_action(request,
                            obj=self.get_object(),
                            action_flag=self.get_destroy_action_flag())
        return response

    @classmethod
    def obj_is_dapp(cls, obj):
        """Check if the object is a dapp."""
        obj_model = cls.get_obj_model(obj).model
        return obj_model in DAPP_MODELS_LIST

    def get_dapp_object(self, obj, dapp=None):
        if dapp:
            return dapp
        elif self.obj_is_dapp(obj):
            return obj
        elif hasattr(self, 'get_dapp'):
            return self.get_dapp()
        raise Exception('The ViewSet need a `get_dapp` function.')

    @classmethod
    def get_obj_model(cls, obj):
        return ContentType.objects.get_for_model(obj)

    def log_action(self, request, obj, action_flag, dapp=None):
        return APILog.objects.create(user=request.user,
                                     content_type=self.get_obj_model(obj),
                                     object_id=obj.pk,
                                     action_flag=action_flag,
                                     dapp=self.get_dapp_object(obj, dapp))
