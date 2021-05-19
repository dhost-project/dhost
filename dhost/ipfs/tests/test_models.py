from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import IPFSDapp, IPFSDeployment

User = get_user_model()


class TestDataMixin:

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user('ifps_user1', 'iuser1@example.com',
                                             'password')

        cls.ipfs1 = IPFSDapp.objects.create(
            source=None,
            command='npm build',
            docker='node:12',
            owner=cls.user1,
            hash='bafybeifx7yeb55armcsxwwitkymga5xf53dxiarykms3ygqic223w5sk3m',
        )

        cls.deploy1 = IPFSDeployment.objects.create(
            dapp=cls.ipfs1,
            hash=cls.ipfs1.hash,
        )


class IPFSModelsTestCase(TestDataMixin, TestCase):

    def test_can_deploy(self):
        deployments_number = self.ipfs1.deployments.all().count()
        self.ipfs1.deploy()
        deployments_number_after = self.ipfs1.deployments.all().count()
        self.assertEqual(deployments_number + 1, deployments_number_after)

    def test_get_public_url(self):
        public_url = self.ipfs1.get_public_url()
        self.assertIn(self.ipfs1.hash, public_url)


class IPFSDeploymentTestCase(TestDataMixin, TestCase):

    def test_str(self):
        self.assertEqual(type(str(self.deploy1)), str)

    def test_can_deploy(self):
        self.deploy1.deploy()

    def test_delete(self):
        deployments_number = IPFSDeployment.objects.all().count()
        self.deploy1.delete()
        deployments_number_after = IPFSDeployment.objects.all().count()
        self.assertEqual(deployments_number - 1, deployments_number_after)
