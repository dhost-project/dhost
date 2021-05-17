from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from rest_framework import viewsets

from .forms import EnvironmentVariableForm
from .models import Build, BuildOptions, Bundle, EnvironmentVariable
from .serializers import (BuildSerializer, BundleSerializer,
                          EnvironmentVariableSerializer)


class BundleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer


class BuildsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class EnvironmentVariableViewSet(viewsets.ModelViewSet):
    queryset = EnvironmentVariable.objects.all()
    serializer_class = EnvironmentVariableSerializer


class BuildOptionsUpdateView(UpdateView):
    # TODO integrate the `EnvironmentVariableListView` has a formset view mixin
    # to be able to edit the environment variables inside the settings
    # in AJAX and without changing views
    model = BuildOptions
    fields = ['command', 'docker']

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


class BundleListView(ListView):
    model = Bundle
    build_options_url_kwarg = 'build_op_pk'

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_queryset(self):
        """Filter queryset to only show the current build options's bundles"""
        return super().get_queryset().filter(
            build__options__pk=self._get_build_options_id())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'build_options_url':
                BuildOptions.objects.get(
                    id=self._get_build_options_id(),).get_absolute_url()
        })
        return context


class BundleDetailView(DetailView):
    model = Bundle

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'bundle_list_url':
                reverse_lazy(
                    'bundle_list',
                    kwargs={'build_op_pk': self.object.build.options.id})
        })
        return context


class BuildListView(ListView):
    model = Build
    build_options_url_kwarg = 'build_op_pk'

    def _get_build_options_id(self):
        return self.kwargs.get(self.build_options_url_kwarg)

    def get_queryset(self):
        """Filter queryset to only show the current build options's builds"""
        return super().get_queryset().filter(
            options__pk=self._get_build_options_id())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'build_options_url':
                BuildOptions.objects.get(
                    id=self._get_build_options_id(),).get_absolute_url()
        })
        return context


class BuildDetailView(DetailView):
    model = Build

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update({
            'build_list_url':
                reverse_lazy('build_list',
                             kwargs={'build_op_pk': self.object.options.id})
        })
        return context
