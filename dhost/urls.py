from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/', include('dhost.users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # apps
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.views.defaults import page_not_found

    def page_not_found_debug(request):
        return page_not_found(request, exception=None)

    urlpatterns += [path('404', page_not_found_debug)]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
