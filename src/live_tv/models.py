from django.db import models


# Create your models here.
class LiveTv(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    coverImage = models.CharField(max_length=200)
    horizontalImage = models.CharField(max_length=200)
    needLogin = models.IntegerField(default=0)
    price = models.IntegerField()
    link = models.CharField(max_length=100)

    class Meta:
        ordering = ['created', '_id']


