from django.urls import path, include

from .api.viewsets import UserList, UserDetails, GroupList


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<pk>/', UserDetails.as_view()),
    path('groups/', GroupList.as_view()),
]
