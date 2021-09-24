from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from dhost.dapps.views import DappViewMixin

from .models import Build, BuildOptions, EnvVar
from .serializers import (
    BuildOptionsSerializer,
    BuildSerializer,
    CreateEnvVarSerializer,
    EnvVarSerializer,
)


class BuildOptionsViewSet(DappViewMixin, viewsets.ModelViewSet):
    queryset = BuildOptions.objects.all()
    serializer_class = BuildOptionsSerializer

    def perform_create(self, serializer):
        # Add `dapp` when creating the buildoptions
        serializer.save(dapp=self.get_dapp())

    @action(detail=True, methods=["get"])
    def build(self, request, pk=None, dapp_slug=None):
        build_options = self.get_object()
        build_options.start_build()
        return Response({"status": "build started."})


class BuildViewMixin(DappViewMixin):
    """Add the ability to filter the queryset, also check for permissions."""

    buildoptions_model_class = BuildOptions
    buildoptions_reverse_name = "buildoptions"

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


class EnvVarViewSet(BuildViewMixin, viewsets.ModelViewSet):
    queryset = EnvVar.objects.all()
    serializer_class = EnvVarSerializer
    create_serializer_class = CreateEnvVarSerializer

    def get_serializer_class(self):
        """Add the ability to write sensitive when creating.

        This allow the user to set the value of sensitive when creating the
        envvar but not edit it when doing an update or partial update.
        """
        if self.action == "create":
            return self.create_serializer_class
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(buildoptions=self.get_buildoptions())
