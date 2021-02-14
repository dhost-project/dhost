from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .core.views import home_view

urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("host/", include("dhost.host.urls")),
]

handler404 = "dhost.core.views.page_not_found_view"

if settings.DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]

