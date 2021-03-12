from django.urls import path

from . import views
from .api import views as api_views

apipatterns = [
    path('users/', api_views.UserList.as_view()),
    path('users/<pk>/', api_views.UserDetails.as_view()),
    path('groups/', api_views.GroupList.as_view()),
]

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path(
        'password/change/',
        views.PasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        'password/change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),
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
    path('settings/', views.settings_view, name='settings'),
    path('settings/delete', views.delete_account, name='delete'),
] + apipatterns
