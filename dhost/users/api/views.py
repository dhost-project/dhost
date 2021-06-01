from oauth2_provider.contrib.rest_framework import (OAuth2Authentication,
                                                    TokenHasScope)
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.GenericViewSet):
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    required_scopes = ['read']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['get'])
    def me(self, request, pk=None):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
