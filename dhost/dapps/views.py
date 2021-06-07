from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from dhost.builds.views import (BuildOptionsViewSet, BuildViewSet,
                                BundleViewSet, EnvironmentVariableViewSet)

from .models import Dapp
from .serializers import AbstractDeploymentSerializer, DappSerializer

User = get_user_model()


class DappViewSet(BuildOptionsViewSet):
    serializer_class = DappSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        user = get_object_or_404(User.objects.all(),
                                 username=self.kwargs['username'])
        print(user)
        filter_kwargs = {
            'owner': user,
            'slug': self.kwargs['dapp__slug'],
        }
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request):
        """Add `owner` when creating the dapp"""
        data = request.data.copy()
        data.update({'owner': self.request.user.id})
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)

    def get_queryset(self):
        """Filter user's apps"""
        user = self.request.user
        return Dapp.objects.filter(owner=user)

    @action(detail=True, methods=['get'])
    def deploy(self, request, pk=None):
        dapp = self.get_object()
        is_success = dapp.deploy()
        if is_success:
            return Response({'status': 'deployment successfull'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AbstractDeploymentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AbstractDeploymentSerializer


class DappBundleViewSet(BundleViewSet):
    pass


class DappBuildViewSet(BuildViewSet):
    pass


class DappEnvironmentVariableViewSet(EnvironmentVariableViewSet):
    pass
