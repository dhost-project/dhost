from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from dhost.utils import get_version


class APIPingView(APIView):
    permission_classes = (AllowAny,)
    name = "Ping"

    def get(self, request, format=None):
        response = {"version": get_version()}
        return Response(response)
