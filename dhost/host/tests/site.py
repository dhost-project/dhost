from django.test import TestCase

from ..models import Site


class SiteTest(TestCase):
    SITE1_NAME = "site1"

    @classmethod
    def setUpTestData(cls):
        Site.objects.create(
            name=cls.SITE1_NAME,
            status=Site.STOPED,
        )

    def test_tech_is_created(self):
        Site.objects.get(name=self.SITE1_NAME)
