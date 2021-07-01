from django.test import TestCase

from dhost.builds.models import BuildOptions


class BuildModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.npm_build = BuildOptions(source=None,
                                     command='npm build',
                                     docker='node:12')
        cls.yarn_build = BuildOptions(source=None,
                                      command='yarn build',
                                      docker='node:12')

    def test_build_options_can_build(self):
        pass
        # npm_build_success, npm_build_bundle = self.npm_build.build()
