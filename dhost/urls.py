from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from .core.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('host/', include('dhost.host.urls')),
    # api
    path('api/', include('dhost.core.api_router')),
    path('api-auth/', include('rest_framework.urls')),
    # apps
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    from django.views.defaults import page_not_found

    def page_not_found_debug(request):
        return page_not_found(request, exception=None)

    urlpatterns += [path('404', page_not_found_debug)]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
