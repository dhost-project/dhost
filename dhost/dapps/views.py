from django.shortcuts import get_object_or_404
from django.conf import settings

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from .models import Bundle, Dapp, Deployment
from .permissions import DappPermission
from .serializers import (
    BundleSerializer,
    DappReadOnlySerializer,
    DappSerializer,
    DeploymentSerializer,
)

import zipfile
from zipfile import ZipFile
import os
import shutil

class DappViewSet(viewsets.ModelViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer
    permission_classes = [DappPermission]
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.user
        return queryset.filter(owner=owner)

    @action(detail=True, methods=["get"])
    def deploy(self, request, slug=None):
        dapp = self.get_object()
        dapp.deploy()
        return Response({"status": "deployment started."})


class DappReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """A list of every dapps, regardless of wich type they are."""

    queryset = Dapp.objects.all()
    serializer_class = DappReadOnlySerializer
    permission_classes = [DappPermission]
    lookup_field = "slug"

    def get_queryset(self):
        queryset = super().get_queryset()
        owner = self.request.user
        return queryset.filter(owner=owner)


class DappViewMixin:
    """Mixin to handle the nested router.

    Retrieve an argument with the dapp slug used to filter the dapps.
    """

    dapp_model_class = Dapp
    dapp_reverse_name = "dapp"  # name of the model field linked to the Dapp
    dapp_url_slug = "dapp_slug"  # URL slug for the Dapp

    def get_dapp(self):
        owner = self.request.user
        slug = self.kwargs[self.dapp_url_slug]
        return get_object_or_404(self.dapp_model_class, owner=owner, slug=slug)

    def get_queryset(self):
        dapp = self.get_dapp()
        filter_kwargs = {self.dapp_reverse_name: dapp}
        return super().get_queryset().filter(**filter_kwargs)


class DeploymentViewSet(DappViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Deployment.objects.all()
    serializer_class = DeploymentSerializer


class BundleViewSet(DappViewMixin, viewsets.ModelViewSet):
    IPFS_MEDIAS = settings.IPFS_MEDIAS
    queryset = Bundle.objects.all()
    serializer_class = BundleSerializer

    def get_queryset(self):
        owner = self.request.user
        queryset = super().get_queryset()
        return queryset.filter(dapp__owner=owner,dapp=self.get_dapp())
    
    def create(self, request,dapp_slug):
        try:
            dapp = self.dapp_model_class.objects.filter(slug=dapp_slug).first()
            media_name = request.data['media'].name
            old_media_url = self.IPFS_MEDIAS + media_name.split('.')[0]
            new_media_url = self.IPFS_MEDIAS + dapp_slug
            if dapp:
                if media_name.endswith('.zip'):
                    zf = ZipFile(request.data['media'], 'r')
                    zf.extractall(self.IPFS_MEDIAS)
                    zf.close()
                    if os.path.exists(new_media_url):
                        shutil.rmtree(new_media_url)
                    os.rename(old_media_url,new_media_url)
            bundle = Bundle.objects.create(dapp = dapp, folder = new_media_url)
            data = BundleSerializer(bundle).data

            return Response(data, status = status.HTTP_201_CREATED)
        except:
            content= {'error': 'Invalid dapp or media'}
            return Response(content , status = status.HTTP_400_BAD_REQUEST)
