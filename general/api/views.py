from rest_framework.response import Response
from general.api.serializers import RatingSerializer, ComicSerializer
from general.models import Comic, Rating
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404


class RatingViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = RatingSerializer
    queryset = RatingSerializer

    def create(self, request, *args, **kwargs):
        comic_id = request.data.get('comic_id')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class ComicViewSet(
    ListModelMixin,
    GenericViewSet,
):
    serializer_class = ComicSerializer
    queryset = Comic.objects.all()

    # def list(self, request, comic_id):
    #     comic = get_object_or_404(Comic, id=comic_id)
    #     ratings = Rating.objects.filter(comic_id=comic_id)
    #     average_rating = ratings.aggregate(models.Avg('value'))['value__avg']

    #     return Response({'rating': average_rating})

    def get_comic_rating(self, request, comic_id=None):
        try:
            comic = Comic.objects.get(id=comic_id)
            rating_value = comic.rating
            return Response({'rating': rating_value})
        except Comic.DoesNotExist:
            return Response({'error': 'Comic does not exist'}, status=status.HTTP_404_NOT_FOUND)
