from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile_img = models.ImageField(upload_to="/profiles/", null=True, blank=True)
    bio = models.CharField(max_length=200)


class Channel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Video(models.Model):
    channel = models.ForeignKey(Channel)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    video = models.FileField(upload_to="/videos/")
    poster = models.ImageField(upload_to="/imgs/")
