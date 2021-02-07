from django.urls import path

from .views import (
    WebsiteListView,
    WebsiteDetailView,
    WebsiteCreateView,
    WebsiteUpdateView,
    WebsiteDeleteView,
)


urlpatterns = [
    path('', WebsiteListView.as_view(), name='website_list'),
    path('new', WebsiteCreateView.as_view(), name='website_create'),
    path('<slug:slug>/', WebsiteDetailView.as_view(), name='website_detail'),
    path('<slug:slug>/edit', WebsiteUpdateView.as_view(), name='website_update'),
    path('<slug:slug>/delete', WebsiteDeleteView.as_view(), name='website_delete'),
]

