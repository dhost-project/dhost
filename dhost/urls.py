from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('oauth2/', include('dhost.oauth2.urls', namespace='oauth2_provider')),
    path('social/', include('social_django.urls', namespace='social')),
    path('u/', include('dhost.users.urls')),
    path('admin/', admin.site.urls),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
