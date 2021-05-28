from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path(
        'password/reset/',
        views.PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'password/reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
    path(
        'settings/',
        views.AccountSettingsView.as_view(),
        name='account_settings',
    ),
    path(
        'settings/password/change/',
        views.PasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        'settings/password/change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),
    path(
        'settings/export_data/',
        views.ExportDataView.as_view(),
        name='export_data',
    ),
    path(
        'settings/delete/',
        views.AccountDeleteView.as_view(),
        name='account_delete',
    ),
    path(
        'settings/delete/done/',
        views.AccountDeleteDoneView.as_view(),
        name='account_delete_done',
    ),
]
