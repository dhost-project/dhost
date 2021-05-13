from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView

from dhost.builds import views as builds_views

from .models import Dapp


class DappCreateView(builds_views.BuildOptionsCreateView):
    model = Dapp
    fields = ['name', 'command', 'docker']
    template_name = 'dapps/dapp_create_form.html'

    def form_valid(self, form):
        """Automatically attribute current user to the build option"""
        build_option = form.save(commit=False)
        if self.request.user.is_authenticated:
            build_option.owner = self.request.user
        return super().form_valid(form)


class DappDetailView(builds_views.BuildOptionsDetailView):
    model = Dapp

    def get_queryset(self):
        """Filter to only show user's Dapps"""
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class DappUpdateView(builds_views.BuildOptionsUpdateView):

    model = Dapp
    fields = ['name', 'command', 'docker']

    def get_queryset(self):
        """Filter to only show user's Dapps"""
        queryset = super().get_queryset()
        queryset = queryset.filter(owner=self.request.user)
        return queryset


class EnvironmentVariableListView(builds_views.EnvironmentVariableListView):
    pass


class EnvironmentVariableCreateView(builds_views.EnvironmentVariableCreateView):
    pass


class DappMixin:
    """Used byt the `BuildOptionsMixin` to retrieve the URL to the builds
    options
    """
    build_op_model = Dapp


class BundleListView(DappMixin, builds_views.BundleListView):
    pass


class BundleDetailView(DappMixin, builds_views.BundleDetailView):
    pass


class BuildListView(DappMixin, builds_views.BuildListView):
    pass


class BuildDetailView(DappMixin, builds_views.BuildDetailView):
    pass


class AbstractDeploymentListView(DappMixin, builds_views.BuildOptionsMixin,
                                 ListView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)


class AbstractDeploymentDetailView(DappMixin, builds_views.BuildOptionsMixin,
                                   DetailView):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_object_build_options(self):
        return self.object.bundle.options
