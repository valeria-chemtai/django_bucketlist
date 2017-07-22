from rest_framework import serializers

from api.models import Bucketlist


class BucketlistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('url', 'pk', 'name')
