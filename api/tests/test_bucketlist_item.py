from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import BucketlistItem


class TestBucketListItem(APITestCase):
    def setUp(self):
        self.create_item_url = reverse('bucketlistitem-list')
        self.create_bucket_url = reverse('bucketlist-list')
        self.bucket = {'name': 'New Bucketlist'}
        self.bucket2 = {'name': 'Another Bucketlist'}
        self.item = {'name': 'New Item'}

    def test_item_creation(self):
        resp1 = self.client.post(self.create_bucket_url, self.bucket)
        self.assertEqual(resp1.status_code, 201)

        item = {'name': 'New Item', 'bucketlist_id': resp1.data['pk']}
        resp2 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp2.status_code, 201)
        self.assertEqual('New Item', resp2.data.get('name'))

        self.assertEqual(BucketlistItem.objects.count(), 1)

    def test_item_duplicate(self):
        resp1 = self.client.post(self.create_bucket_url, self.bucket)
        self.assertEqual(resp1.status_code, 201)

        item = {'name': 'New Item', 'bucketlist_id': resp1.data['pk']}
        resp2 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp2.status_code, 201)

        resp3 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp3.status_code, 400)

        self.assertEqual(BucketlistItem.objects.count(), 1)

    def test_item_duplicate_different_bucket_id(self):
        resp1 = self.client.post(self.create_bucket_url, self.bucket)
        self.assertEqual(resp1.status_code, 201)

        resp2 = self.client.post(self.create_bucket_url, self.bucket2)
        self.assertEqual(resp1.status_code, 201)

        item = {'name': 'New Item', 'bucketlist_id': resp1.data['pk']}
        resp3 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp3.status_code, 201)

        item2 = {'name': 'New Item', 'bucketlist_id': resp2.data['pk']}
        resp4 = self.client.post(self.create_item_url, item2)
        self.assertEqual(resp4.status_code, 400)

        self.assertEqual(BucketlistItem.objects.count(), 1)

    def test_item_update(self):
        resp1 = self.client.post(self.create_bucket_url, self.bucket)
        self.assertEqual(resp1.status_code, 201)

        item = {'name': 'New Item', 'bucketlist_id': resp1.data['pk']}
        new_item_name = {'name': 'Update Item',
                         'bucketlist_id': resp1.data['pk']}
        resp2 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp2.status_code, 201)

        update_item_url = reverse(
            'bucketlistitem-detail', kwargs={'pk': resp2.data['pk']})
        resp3 = self.client.put(update_item_url, new_item_name)
        self.assertEqual(resp3.status_code, 200)
        self.assertEqual('Update Item', resp3.data.get('name'))

        self.assertEqual(BucketlistItem.objects.count(), 1)

    def test_item_delete(self):
        resp1 = self.client.post(self.create_bucket_url, self.bucket)
        self.assertEqual(resp1.status_code, 201)

        item = {'name': 'New Item', 'bucketlist_id': resp1.data['pk']}
        resp2 = self.client.post(self.create_item_url, item)
        self.assertEqual(resp2.status_code, 201)

        update_item_url = reverse(
            'bucketlistitem-detail', kwargs={'pk': resp2.data['pk']})
        resp3 = self.client.delete(update_item_url)
        self.assertEqual(resp3.status_code, 204)

        self.assertEqual(BucketlistItem.objects.count(), 0)
