from dhost.builds.views import BuildOptionsViewSet

from .models import Dapp
from .serializers import DappSerializer


class DappViewSet(BuildOptionsViewSet):
    queryset = Dapp.objects.all()
    serializer_class = DappSerializer
