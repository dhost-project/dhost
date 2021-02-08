from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('host/', include('dhost.host.urls')),
]

handler404 = 'dhost.core.views.page_not_found_view'
