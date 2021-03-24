from django.urls import path

from . import views

urlpatterns = [
    path(
        '<int:pk>/settings/',
        views.BuildOptionsUpdateView.as_view(),
        name='build_options_update',
    ),
    path(
        '<int:build_op_pk>/env_vars/',
        views.EnvironmentVariableListView.as_view(),
        name='env_vars_list',
    ),
    path(
        '<int:build_op_pk>/env_vars/new',
        views.EnvironmentVariableCreateView.as_view(),
        name='env_vars_create',
    ),
    path(
        '<int:build_op_pk>/bundles/',
        views.BundleListView.as_view(),
        name='bundle_list',
    ),
    path(
        'bundle/<uuid:pk>/',
        views.BundleDetailView.as_view(),
        name='bundle_detail',
    ),
    path(
        '<int:build_op_pk>/builds/',
        views.BuildListView.as_view(),
        name='build_list',
    ),
    path(
        'build/<uuid:pk>/',
        views.BuildDetailView.as_view(),
        name='build_detail',
    ),
]
