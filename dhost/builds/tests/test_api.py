from django.test import override_settings
from django.urls import reverse
from rest_framework import status
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


@override_settings(ROOT_URLCONF="dhost.builds.tests.urls")
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
        url = reverse('build-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # TODO to change so that it only returns the amount of builds related
        # to a build options
        self.assertEqual(Build.objects.count(), len(response.data))

    def test_build_retrieve(self):
        pass


class BundleAPITestCase(APITestCase):

    def test_bundle_list(self):
        url = reverse('bundle-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_bundle_retrieve(self):
        pass


class EnvironmentVariableAPITestCase(APITestCase):

    def test_envvar_list(self):
        url = reverse('environmentvariable-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_envvar_retrieve(self):
        pass
