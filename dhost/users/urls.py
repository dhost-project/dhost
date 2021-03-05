from django.urls import include, path

from . import views

apipatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<pk>/', views.UserDetails.as_view()),
    path('groups/', views.GroupList.as_view()),
]

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
] + apipatterns
