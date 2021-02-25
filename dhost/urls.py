from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/', include('dhost.users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    # apps
    path('admin/', admin.site.urls),
]

if settings.ENABLE_DEBUG_TOOLBAR:
    import debug_toolbar

    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
