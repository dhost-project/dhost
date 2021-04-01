from dhost.builds import views as builds_views

from .models import Dapp


class DappUpdateView(builds_views.BuildOptionsUpdateView):

    model = Dapp
    fields = ['name', 'command', 'docker']
    template_name = 'builds/buildoptions_form.html'

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
