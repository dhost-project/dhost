from django.test import TestCase

from ..models import Site


class SiteTest(TestCase):
    def setUp(self):
        Site.objects.create(
            name='site1',
            status=Site.STOPED,
        )

    def test_tech_is_created(self):
        s1 = Site.objects.get(name='site1')

