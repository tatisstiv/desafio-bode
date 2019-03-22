from django.conf import settings
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    rented = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='movies')


