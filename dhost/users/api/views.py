from django.contrib.auth.models import Group
from oauth2_provider.contrib.rest_framework import (
    OAuth2Authentication, TokenHasReadWriteScope, TokenHasScope
)
from rest_framework import generics, permissions

from ..models import User
from .serializers import GroupSerializer, UserSerializer


class UserList(generics.ListCreateAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
