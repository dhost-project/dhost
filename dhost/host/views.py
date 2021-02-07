from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Website, File


class WebsiteListView(ListView):
    model = Website


class WebsiteDetailView(DetailView):
    model = Website


class WebsiteCreateView(CreateView):
    model = Website


class WebsiteUpdateView(UpdateView):
    model = Website


class WebsiteDeleteView(DeleteView):
    model = Website

