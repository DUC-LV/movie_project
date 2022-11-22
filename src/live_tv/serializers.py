from rest_framework import serializers
from .models import LiveTv


class LiveTvSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveTv
        fields = [
            'created',
            '_id',
            'name',
            'description',
            'slug',
            'type',
            'coverImage',
            'horizontalImage',
            'needLogin',
            'price',
            'link'
        ]
