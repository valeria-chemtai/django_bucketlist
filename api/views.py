# Create your views here.
from rest_framework import viewsets

from api.models import Bucketlist
from api.serializers import BucketlistSerializer


class BucketlistViewSet(viewsets.ModelViewSet):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
