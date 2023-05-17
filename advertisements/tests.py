from unittest import TestCase
from rest_framework.test import APIClient


class TestSampleViews(TestCase):
    def test_views(self):
        url = '/api/adv/'
        client = APIClient()
        response = client.get(url)
        self.assertEqual(response.status_code, 200 )
