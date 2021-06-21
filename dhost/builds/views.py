from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.dapps.views import DappViewMixin
from dhost.logs.views_mixins import APILogViewSetMixin

from .models import Build, BuildOptions, EnvVar
from .serializers import (BuildOptionsSerializer, BuildSerializer,
                          EnvVarSerializer)


class BuildOptionsViewSet(APILogViewSetMixin, DappViewMixin,
                          viewsets.ModelViewSet):
    queryset = BuildOptions.objects.all()
    serializer_class = BuildOptionsSerializer

    def perform_create(self, serializer):
        # Add `dapp` when creating the buildoptions
        serializer.save(dapp=self.get_dapp())

    @action(detail=True, methods=['get'])
    def build(self, request, pk=None):
        build_options = self.get_object()
        is_success, _ = build_options.build()
        if is_success:
            return Response({'status': 'build started.'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BuildViewMixin(DappViewMixin):
    """
    Extend the DappViewMixin to add the ability to filter the queryset using
    from the URL, also check for permissions.
    """

    buildoptions_model_class = BuildOptions
    buildoptions_reverse_name = 'buildoptions'

    def get_buildoptions(self):
        dapp = self.get_dapp()
        return get_object_or_404(self.buildoptions_model_class, dapp=dapp)

    def get_queryset(self):
        buildoptions = self.get_buildoptions()
        filter_kwargs = {self.buildoptions_reverse_name: buildoptions}
        return self.queryset.filter(**filter_kwargs)


class BuildViewSet(BuildViewMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class EnvVarViewSet(APILogViewSetMixin, BuildViewMixin, viewsets.ModelViewSet):
    queryset = EnvVar.objects.all()
    serializer_class = EnvVarSerializer

    def perform_create(self, serializer):
        serializer.save(buildoptions=self.get_buildoptions())
