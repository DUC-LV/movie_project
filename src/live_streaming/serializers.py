from rest_framework import serializers
from .models import LiveStreaming


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveStreaming
        fields = [
            'created',
            '_id',
            'title',
            'message',
            'itemId',
            'itemType',
            'urlImage'
        ]
