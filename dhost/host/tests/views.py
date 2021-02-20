from django.test import RequestFactory, TestCase

from ..views import SiteCreateView, SiteDeleteView, SiteDetailView, SiteListView, SiteUpdateView


class SiteListViewTest(TestCase):

    def test_environment_set_in_context(self):
        request = RequestFactory().get('/host/')
        view = SiteListView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('site_list', context)


class SiteDetailViewTest(TestCase):

    def test_environment_set_in_context(self):
        request = RequestFactory().get('/host/')
        view = SiteDetailView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('site_list', context)


class SiteCreateViewTest(TestCase):

    def test_environment_set_in_context(self):
        request = RequestFactory().get('/host/')
        view = SiteCreateView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('site_list', context)


class SiteUpdateViewTest(TestCase):

    def test_environment_set_in_context(self):
        request = RequestFactory().get('/host/')
        view = SiteUpdateView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('site_list', context)


class SiteDeleteViewTest(TestCase):

    def test_environment_set_in_context(self):
        request = RequestFactory().get('/host/')
        view = SiteDeleteView()
        view.setup(request)

        context = view.get_context_data()
        self.assertIn('site_list', context)
