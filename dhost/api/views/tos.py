from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny


class APITermsOfServiceView(TemplateView):
    permission_classes = (AllowAny,)
    name = "TermsOfService"
    template_name = "api_tos.html"
