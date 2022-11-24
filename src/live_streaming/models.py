from django.db import models


# Create your models here.
class LiveStreaming(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.IntegerField()
    title = models.CharField(max_length=200)
    message = models.CharField(max_length=300)
    itemId = models.IntegerField(primary_key=True)
    itemType = models.CharField(max_length=100)
    urlImage = models.CharField(max_length=200)

    class Meta:
        ordering = ['created']
