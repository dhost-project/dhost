from django.test import TestCase

from .models import Technology, File, Website


class TechnologyTest(TestCase):
    def setUp(self):
        Technology.objects.create(name='tech1')

    def test_tech_is_created(self):
        t1 = Technology.objects.get(name='tech1')

