from django.conf import settings
from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=200)
    rented = models.BooleanField(default=False)
    cover_image = models.ImageField(upload_to='movies')


    def rent(self):
        self.rented = True
        self.save()