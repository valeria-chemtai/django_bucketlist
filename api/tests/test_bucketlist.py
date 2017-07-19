from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import BucketList


class TestBucketList(APITestCase):
    # def setUp(self):

    # 	self.view_url = reverse('bucketlist-detail')

    def test_bucketlist_creation(self):
        self.create_url = reverse('bucketlist-list')
        data = {'name': 'New Bucketlist'}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('New Bucketlist', response.content)

    def test_bucketlist_display(self):
        pass

    def test_bucketlist_edit(self):
        pass

    def test_bucketlist_delete(self):
