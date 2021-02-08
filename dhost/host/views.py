from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Site


class SiteListView(ListView):
    model = Site


class SiteDetailView(DetailView):
    model = Site


class SiteCreateView(CreateView):
    model = Site


class SiteUpdateView(UpdateView):
    model = Site


class SiteDeleteView(DeleteView):
    model = Site

