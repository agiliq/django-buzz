from django.test import TestCase, Client
from pystories.models import NewsTopic

class TestViews(TestCase):
	def setUp(self):
		self.c = Client()
		self.topic = NewsTopic.objects.create(title="django", slug="django")

	def test_index(self):
		resp = self.c.get("/pystories/")

		self.assertEqual(resp.status_code, 200)