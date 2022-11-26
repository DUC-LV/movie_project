from rest_framework import serializers
from .models import TopicFilm, ListFilm


class TopicFilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListFilm
        fields = ['created', '_id', 'name', 'description', 'slug', 'type', 'itemType']


class ListFilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = TopicFilm
        fields = ['created', '_id', 'name', 'coverImage', 'coverImageH', 'type', 'description', 'slug', 'link', 'model_chaID']
