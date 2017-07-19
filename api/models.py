from django.db import models

# Create your models here.


class BucketList(models.Model):
    name = models.Charfield(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
