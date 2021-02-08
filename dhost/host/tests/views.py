from django.test import RequestFactory, TestCase

from ..views import SiteCreateView, SiteDeleteView, SiteDetailView, SiteListView, SiteUpdateView


class SiteListViewTest(TestCase):
    def test_environment_set_in_context(self):
        request = RequestFactory().get("/host/")
        view = SiteListView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn("site_list", context)

