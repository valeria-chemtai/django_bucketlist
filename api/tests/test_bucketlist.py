from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import Bucketlist


class TestBucketList(APITestCase):
    def setUp(self):
        self.create_url = reverse('bucketlist-list')
        self.data = {'name': 'New Bucketlist'}

    def test_bucketlist_creation(self):
        resp = self.client.post(self.create_url, self.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual('New Bucketlist', resp.data.get('name'))
        self.assertIn('New Bucketlist', str(resp.data))

    def test_bucketlist_view(self):
        data2 = {'name': 'Another Bucketlist'}
        create_resp1 = self.client.post(self.create_url, self.data)
        self.assertEqual(create_resp1.status_code, 201)
        create_resp2 = self.client.post(self.create_url, data2)
        self.assertEqual(create_resp2.status_code, 201)
        view_resp = self.client.get(self.create_url)
        self.assertEqual(view_resp.status_code, 200)
        self.assertIn('New', str(view_resp.data))
        self.assertIn('Another', str(view_resp.data))
        self.assertEqual(Bucketlist.objects.count(), 2)

    def test_bucketlist_duplicate(self):
        resp1 = self.client.post(self.create_url, self.data)
        self.assertEqual(resp1.status_code, 201)
        resp2 = self.client.post(self.create_url, self.data)
        self.assertEqual(resp2.status_code, 400)
        self.assertEqual(Bucketlist.objects.count(), 1)

    def test_bucketlist_update(self):
        new_data = {'name': 'Updated Bucketlist'}
        resp1 = self.client.post(self.create_url, self.data)
        self.assertEqual(resp1.status_code, 201)
        # import ipdb; ipdb.set_trace()
        url = reverse('bucketlist-detail', None, {resp1.data['pk']})
        resp2 = self.client.put(url, new_data)
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(Bucketlist.objects.count(), 1)
        self.assertEqual('Updated Bucketlist', resp2.data.get('name'))

    def test_bucketlist_delete(self):
        resp1 = self.client.post(self.create_url, self.data)
        self.assertEqual(resp1.status_code, 201)
        url = reverse('bucketlist-detail', None, {resp1.data['pk']})
        resp2 = self.client.delete(url)
        self.assertEqual(resp2.status_code, 204)
        self.assertEqual(Bucketlist.objects.count(), 0)
