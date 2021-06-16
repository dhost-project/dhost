from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Build, EnvVar
from .serializers import BuildSerializer, EnvVarSerializer


class BuildOptionsViewSet(viewsets.ModelViewSet):

    @action(detail=True, methods=['get'])
    def build(self, request, pk=None):
        build_options = self.get_object()
        is_success, _ = build_options.build()
        if is_success:
            return Response({'status': 'build started.'})
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BuildViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Build.objects.all()
    serializer_class = BuildSerializer


class EnvVarViewSet(viewsets.ModelViewSet):
    queryset = EnvVar.objects.all()
    serializer_class = EnvVarSerializer
