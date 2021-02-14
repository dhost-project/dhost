from django.test import TestCase

from ..models import File, Technology


class FileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        tf1 = Technology.objects.create(name="tech_for_file1")

        File.objects.create(
            name="file1",
            technology=tf1,
            url="www.test.com",
            content="<h1>Title</h1>",
        )

    def test_tech_is_created(self):
        File.objects.get(name="file1")
