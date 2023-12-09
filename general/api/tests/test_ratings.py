from django.test import TestCase
from django.contrib.auth.models import User
from general.models import Comic, Rating
from general.api.views import RatingViewSet, ComicViewSet


class RatingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.comic = Comic.objects.create(title='Test Comic', author='Test Author')

    def test_create_rating_and_update_rating(self):
        value = 4
        request_data = {
            'comic_id': self.comic.id,
            'user_id': self.user.id,
            'VALUE': value
        }
        create_rating_view = RatingViewSet()
        create_rating_view.request = self.client.post('/api/ratings/', data=request_data)
        create_rating_view.perform_create(create_rating_view.get_serializer())

        updated_comic = Comic.objects.get(id=self.comic.id)
        self.assertEqual(updated_comic.rating, value)

    def test_get_average_comic_rating(self):
        Rating.objects.create(comic_id=self.comic.id, user_id=self.user.id, value=4)
        Rating.objects.create(comic_id=self.comic.id, user_id=self.user.id, value=3)
        Rating.objects.create(comic_id=self.comic.id, user_id=self.user.id, value=5)

        comic_rating_view = ComicViewSet()
        comic_rating_view.request = self.client.get(f'/api/comics/{self.comic.id}/rating/')
        response = comic_rating_view.retrieve(comic_rating_view.request)
        self.assertEqual(response.data['rating'], 4)
