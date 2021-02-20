from django.test import TestCase

from ..models import Technology


class TechnologyTest(TestCase):
    fixtures = ['technologies.json']

    def test_tech_is_created(self):
        Technology.objects.get(pk=1)
