from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    added_on = models.DateField()

    def __str__(self):
        return self.title


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username