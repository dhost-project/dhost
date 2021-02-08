from django.test import TestCase

from ..models import File, Technology


class FileTest(TestCase):
    def setUp(self):
        Technology.objects.create(name='tech_for_file1')
        tf1 = Technology.objects.get(name='tech_for_file1')

        File.objects.create(
            name='file1',
            technology=tf1,
            url='www.test.com',
            content='<h1>Title</h1>',
        )

    def test_tech_is_created(self):
        f1 = File.objects.get(name='file1')
