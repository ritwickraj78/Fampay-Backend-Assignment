from rest_framework import serializers

from api.models import YoutubeVideo


class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ['title', 'description', 'thumbnail_url', 'published_date']
