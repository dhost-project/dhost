from django.contrib.contenttypes.models import ContentType

from .models import APILog


class APILogViewSetMixin:
    """
    Add the ability to log actions, logged actions are on state changing calls
    from viewsets (create, update, partial_update, destroy).
    """

    log_on_create = True
    create_action_flag = None
    log_on_update = True
    update_action_flag = None
    log_on_partial_update = True
    partial_update_action_flag = None
    log_on_destroy = True
    destroy_action_flag = None
    # True if the current ViewSet is for a Dapp object
    object_is_dapp = False

    def get_create_action_flag(self):
        if self.create_action_flag:
            return self.create_action_flag
        raise Exception('Please provide a `create_action_flag`.')

    def perform_create(self, serializer):
        # we need the object to create the log
        self.obj = serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if self.log_on_create:
            self.log_action(
                request,
                obj=self.obj,
                action_flag=self.get_create_action_flag(),
            )
        return response

    def get_update_action_flag(self):
        if self.update_action_flag:
            return self.update_action_flag
        raise Exception('Please provide an `update_action_flag`.')

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if self.log_on_update:
            self.log_action(
                request,
                obj=self.get_object(),
                action_flag=self.get_update_action_flag(),
            )
        return response

    def get_partial_update_action_flag(self):
        if self.partial_update_action_flag:
            return self.partial_update_action_flag
        if self.update_action_flag:
            return self.update_action_flag
        raise Exception('Please provide a `partial_update_action_flag` or '
                        '`update_action_flag`.')

    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        if self.log_on_partial_update:
            self.log_action(
                request,
                obj=self.get_object(),
                action_flag=self.get_partial_update_action_flag(),
            )
        return response

    def get_destroy_action_flag(self):
        if self.destroy_action_flag:
            return self.destroy_action_flag
        raise Exception('Please provide a `destroy_action_flag`.')

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        if self.log_on_destroy:
            self.log_action(
                request,
                obj=self.get_object(),
                action_flag=self.get_destroy_action_flag(),
            )
        return response

    def get_dapp_object(self, obj, dapp=None):
        if dapp:
            return dapp
        elif self.object_is_dapp:
            return obj
        elif hasattr(self, 'get_dapp'):
            return self.get_dapp()
        raise Exception(
            'The ViewSet either need a `get_dapp` function or needs to be a '
            'dapp and have the `object_is_dapp` parameter set to True.')

    @classmethod
    def get_obj_content_type(cls, obj):
        return ContentType.objects.get_for_model(obj)

    def log_action(self, request, obj, action_flag, dapp=None):
        return APILog.objects.create(
            user=request.user,
            content_type=self.get_obj_content_type(obj),
            object_id=obj.pk,
            action_flag=action_flag,
            dapp=self.get_dapp_object(obj, dapp),
        )
