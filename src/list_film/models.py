from django.db import models


# Create your models here.
class TopicFilm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    itemType = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']


class ListFilm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    coverImage = models.CharField(max_length=200)
    coverImageH = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    model_chaID = models.ForeignKey(TopicFilm, on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
