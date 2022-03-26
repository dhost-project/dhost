from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase, override_settings, tag

from dhost.ipfs.models import IPFSDapp, IPFSDeployment

User = get_user_model()


class TestDataMixin:
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            "ifps_user1", "iuser1@example.com", "password"
        )
        cls.ipfs1 = IPFSDapp.objects.create(
            slug="dhost",
            owner=cls.user1,
            ipfs_hash="bafybeifx7yeb55armcsxwwitkymga5xf53dxiarykms3ygqic223w5s"
            "k3m",
        )
        cls.deploy1 = IPFSDeployment.objects.create(
            dapp=cls.ipfs1,
            ipfs_hash=cls.ipfs1.ipfs_hash,
        )


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class IPFSModelsTestCase(TestDataMixin, TestCase):

    # TODO mock the IPFS deploy function
    @tag("core", "slow")
    def test_can_deploy(self):
        pass
        # deployments_number = self.ipfs1.deployments.all().count()
        # self.ipfs1.deploy()
        # deployments_number_after = self.ipfs1.deployments.all().count()
        # self.assertEqual(deployments_number + 1, deployments_number_after)

    @tag("fast")
    def test_get_public_url(self):
        public_url = self.ipfs1.get_public_url()
        self.assertIn(self.ipfs1.ipfs_hash, public_url)


@override_settings(MEDIA_ROOT=settings.TEST_MEDIA_ROOT)
class IPFSDeploymentTestCase(TestDataMixin, TestCase):
    @tag("fast")
    def test_str(self):
        self.assertEqual(type(str(self.deploy1)), str)

    # @tag("core", "slow")
    # def test_can_deploy(self):
    #     self.deploy1.deploy()

    @tag("slow")
    def test_delete(self):
        deployments_number = IPFSDeployment.objects.all().count()
        self.deploy1.delete()
        deployments_number_after = IPFSDeployment.objects.all().count()
        self.assertEqual(deployments_number - 1, deployments_number_after)
