from rest_framework import serializers

from api.models import Bucketlist, BucketlistItem


class BucketlistSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='bucketlistitem-detail')

    class Meta:
        model = Bucketlist
        fields = ('url', 'pk', 'name', 'date_created',
                  'date_modified', 'items')


class BucketlistItemSerializer(serializers.HyperlinkedModelSerializer):
    bucketlist_id = serializers.SlugRelatedField(
        queryset=Bucketlist.objects.all(), slug_field='pk')

    class Meta:
        model = BucketlistItem
        depth = 4
        fields = ('url', 'pk', 'name', 'bucketlist_id', 'date_created',
                  'date_modified')
