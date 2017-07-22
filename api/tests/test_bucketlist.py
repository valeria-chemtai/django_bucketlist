from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import Bucketlist


class TestBucketList(APITestCase):
    def setUp(self):
        self.create_url = reverse('bucketlist-list')

    # 	self.view_url = reverse('bucketlist-detail')

    def test_bucketlist_creation(self):
        data = {'name': 'New Bucketlist'}
        resp = self.client.post(self.create_url, data)
        # import ipdb; ipdb.set_trace()
        self.assertEqual(resp.status_code, 201)
        self.assertIn('New Bucketlist', resp.content)
