from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    rating = models.FloatField(default=0)


class Rating(models.Model):
    comic_id = models.ForeignKey(Comic, related_name='ratings', on_delete=models.CASCADE)
    user_id = models.CharField(max_length=100)
    VALUE = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
