from rest_framework import routers

from api.views import BucketlistViewSet

router = routers.DefaultRouter()

router.register(r'bucketlists', BucketlistViewSet)

urlpatterns = router.urls
