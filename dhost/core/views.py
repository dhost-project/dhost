from django.http import HttpResponseNotFound
from django.template.response import TemplateResponse
from sentry_sdk import capture_message
from django.core.mail import send_mail


def home_view(request):
    return TemplateResponse(request, "home/home.html", {})


def page_not_found_view(*args, **kwargs):
    capture_message("Page not found!", level="error")
    return HttpResponseNotFound("Not found")

