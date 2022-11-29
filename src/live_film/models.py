from django.db import models


# Create your models here.
class LiveFilm(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    _id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    coverImage = models.CharField(max_length=200)
    coverImageH = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']
