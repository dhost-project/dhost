from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import EnvironmentVariableForm
from .models import Build, BuildOptions, Bundle, EnvironmentVariable


class BuildOptionsDetailView(DetailView):
    """Build options overview, show logs, links to builds, bundles settings"""
    model = BuildOptions

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class BuildOptionsUpdateView(UpdateView):
    # TODO integrate the `EnvironmentVariableListView` has a formset view mixin
    # to be able to edit the environment variables inside the settings
    # in AJAX and without changing views
    model = BuildOptions
    fields = ['command', 'docker']

    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(form=form))


class EnvironmentVariableListView(ListView):
    # TODO use formset to display every variables forms on this page
    # TODO add the ability to add new environment variables with AJAX from this
    # page, it will post on the `EnvironmentVariableCreateView` view
    # TODO transform into a mixin to be used in the `BuildOptionsUpdateView`
    model = EnvironmentVariable
    build_options_url_kwarg = 'build_op_pk'

    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_queryset(self):
        """
        Filter queryset to only show the current build options's environment
        variables
        """
        queryset = super().get_queryset()
        queryset = queryset.filter(options__pk=self._get_build_options_id())
        return queryset


class EnvironmentVariableCreateView(CreateView):
    model = EnvironmentVariable
    form_class = EnvironmentVariableForm
    build_options_url_kwarg = 'build_op_pk'

    @method_decorator(sensitive_post_parameters())
    @method_decorator(csrf_protect)
    @method_decorator(login_required)
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'options_id': self._get_build_options_id()})
        return kwargs

    def get_success_url(self):
        return reverse_lazy(
            'env_vars_list',
            kwargs={'build_op_pk': self._get_build_options_id()})


class BuildOptionsMixin:
    """A mixin to add the current object's build options URL, the URL is passed
    in the context with the name `build_options_url`.
    """
    build_op_model = BuildOptions

    def _get_build_options_id(self):
        """Overwrite this function to get the build URL from an id"""
        return None

    def _get_object_build_options(self):
        """Return the object's options"""
        if hasattr(self.object, 'options'):
            return self.object.options
        return None

    def _get_build_options(self):
        """Return a build options object"""
        build_op_id = self._get_build_options_id()
        if build_op_id:
            return self.build_op_model.objects.get(id=build_op_id)
        return self._get_object_build_options()

    def get_build_options_url(self):
        """Return the build options object's URL"""
        build_op = self._get_build_options()
        if build_op and hasattr(build_op, 'get_absolute_url'):
            return build_op.get_absolute_url()
        return None

    def get_context_data(self, *args, **kwargs):
        """Add the build options URL to the context"""
        context = super().get_context_data(*args, **kwargs)
        context.update({'build_options_url': self.get_build_options_url()})
        return context


class BundleListView(BuildOptionsMixin, ListView):
    model = Bundle
    build_options_url_kwarg = 'build_op_pk'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_queryset(self):
        """Filter queryset to only show the current build options's bundles"""
        return super().get_queryset().filter(
            build__options__pk=self._get_build_options_id())


class BundleDetailView(BuildOptionsMixin, DetailView):
    model = Bundle

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'bundle_list_url':
                reverse_lazy(
                    'bundle_list',
                    kwargs={'build_op_pk': self.object.build.options.id})
        })
        return context


class BuildListView(BuildOptionsMixin, ListView):
    model = Build
    build_options_url_kwarg = 'build_op_pk'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_queryset(self):
        """Filter queryset to only show the current build options's builds"""
        return super().get_queryset().filter(
            options__pk=self._get_build_options_id())


class BuildDetailView(BuildOptionsMixin, DetailView):
    model = Build

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'build_list_url':
                reverse_lazy('build_list',
                             kwargs={'build_op_pk': self.object.options.id})
        })
        return context
