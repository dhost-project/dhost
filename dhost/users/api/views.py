from oauth2_provider.contrib.rest_framework import (OAuth2Authentication,
                                                    TokenHasScope)
from rest_framework import generics

from ..models import User
from .serializers import UserSerializer


class UserDetails(generics.RetrieveAPIView):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer
