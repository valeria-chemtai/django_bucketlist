import graphene

from graphene_django.types import DjangoObjectType
from . models import Bucketlist, BucketlistItem


class BucketlistType(DjangoObjectType):
    class Meta:
        model = Bucketlist


class BucketlistItemType(DjangoObjectType):
    class Meta:
        model = BucketlistItem


class Query(graphene.AbstractType):
    all_bucketlists = graphene.List(BucketlistType)
    all_bucketlist_items = graphene.List(BucketlistItemType)

    def resolve_all_bucketlists(self, info, **kwargs):
        return Bucketlist.objects.all()

    def resolve_all_bucketlist_items(self, info, **kwargs):
        return BucketlistItem.objects.select_related('items').all()
