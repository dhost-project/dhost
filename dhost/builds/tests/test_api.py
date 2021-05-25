from django.test import override_settings
from rest_framework.test import APITestCase

from ..models import Build, BuildOptions


class TestDataMixin:

    @classmethod
    def setUpTestData(cls):
        cls.bo1 = BuildOptions.objects.create(source=None,
                                              command='npm build',
                                              docker='node:12')

        # Build
        cls.build1 = Build.objects.create(options=cls.bo1,
                                          is_success=False,
                                          logs='0')
        cls.build2 = Build.objects.create(options=cls.bo1,
                                          is_success=True,
                                          logs='1')


@override_settings(ROOT_URLCONF='dhost.builds.tests.urls')
class BuildOptionsAPITest(TestDataMixin, APITestCase):

    def test_build_options_create(self):
        # url = reverse('options-list')
        pass

    def test_build_options_can_build(self):
        pass

    def test_build_options_retrieve(self):
        pass

    def test_build_options_list(self):
        pass


class BuildAPITestCase(TestDataMixin, APITestCase):

    def test_build_list(self):
        pass

    def test_build_retrieve(self):
        pass


class BundleAPITestCase(APITestCase):

    def test_bundle_list(self):
        pass

    def test_bundle_retrieve(self):
        pass


class EnvironmentVariableAPITestCase(APITestCase):

    def test_envvar_list(self):
        pass

    def test_envvar_retrieve(self):
        pass
