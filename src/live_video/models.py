from django.db import models


# Create your models here.
class LiveVideo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    durationStr = models.CharField(max_length=100)
    coverImage = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']