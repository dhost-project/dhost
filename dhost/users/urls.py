from django.urls import include, path

from .views import GroupList, UserDetails, UserList

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]
