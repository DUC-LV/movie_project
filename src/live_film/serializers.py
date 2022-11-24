from rest_framework import serializers
from .models import LiveFilm


class LiveFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveFilm
        fields = [
            'created',
            '_id',
            'name',
            'coverImage',
            'coverImageH',
            'description',
            'slug',
            'type',
            'link',
        ]
