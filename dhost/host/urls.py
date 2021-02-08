from django.urls import path

from .views import SiteCreateView, SiteDeleteView, SiteDetailView, SiteListView, SiteUpdateView

urlpatterns = [
    path("", SiteListView.as_view(), name="website_list"),
    path("new", SiteCreateView.as_view(), name="website_create"),
    path("<slug:slug>/", SiteDetailView.as_view(), name="website_detail"),
    path("<slug:slug>/edit", SiteUpdateView.as_view(), name="website_update"),
    path("<slug:slug>/delete", SiteDeleteView.as_view(), name="website_delete"),
]

