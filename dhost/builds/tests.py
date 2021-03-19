from django.test import TestCase

from .models import BuildOptions


class BuildModelTest(TestCase):

    def setUp(self):
        self.npm_build = self.create_build_otpions()
        self.yarn_build = self.create_build_otpions(command='yarn build')

    def create_build_otpions(self,
                             source=None,
                             command='npm build',
                             docker='node:12'):
        return BuildOptions(source=source, command=command, docker=docker)

    def test_build_options_can_build(self):
        pass
        # npm_build_success, npm_build_bundle = self.npm_build.build()
