from rest_framework import serializers
from general.models import Comic, Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'id',
            'comic_id',
            'user_id',
            'VALUE',
        )


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = (
            'id',
            'title',
            'author',
            'rating',
        )
