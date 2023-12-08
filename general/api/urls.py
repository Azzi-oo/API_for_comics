from rest_framework.routers import SimpleRouter
from general.api.views import RatingViewSet, ComicViewSet
from django.urls import path
from rest_framework import routers


router = SimpleRouter()
router.register(r'ratings', RatingViewSet, basename="ratings")
router.register(r'comics', ComicViewSet, basename="comics")

urlpatterns = [
    *router.urls,
    path('comics/<int:comic_id>/rating/', ComicViewSet.as_view({'get': 'get_comic_rating'}), name='comic-rating'),
]

urlpatterns = router.urls
