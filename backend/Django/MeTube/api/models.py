from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from django.dispatch import receiver
from django.db.models.signals import post_save 
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profiles/", null=True, blank=True)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username + "'s profile"


class Channel(models.Model):
    subscribers = models.ManyToManyField(User, through=u"Subscription", related_name="subscriptions")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Video(models.Model):
    channel = models.ForeignKey(Channel, models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    video = models.FileField(upload_to="videos/")
    poster = models.ImageField(upload_to="imgs/")

    def __str__(self):
        return self.title

class Comment(models.Model):
    # both User and Video models have access to
    # the comments through their `comments` property
    commenter = models.ForeignKey(User, models.CASCADE ,related_name="comments")
    video = models.ForeignKey(Video, models.CASCADE ,related_name="comments")
    comment_text = models.CharField(max_length=300)

    def __str__(self):
        return self.comment_text

class Notification(models.Model):
    status_choices = [
        ("e", "error"),
        ("i", "info"),
        ("s", "success"),
    ]

    text = models.CharField(max_length=300)
    status = models.CharField(max_length=10, choices = status_choices)
    seen = models.BooleanField(default=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return  self.status + self.text


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, models.CASCADE)
    subscribed_channel = models.ForeignKey(Channel, models.CASCADE)
    subscription_date = models.DateField()
    receive_notifications = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.subscription_date = now().date()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.subscriber.username + " is subscribing  " + self.subscribed_channel.name

@receiver(post_save, sender=User)
def generateAuthToken(sender, instance=None, created=False, **kwargs):
    """ Automatically generates tokens for users """
    if created:
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def createUserProfile(sender, instance=None, created=False, **kwargs):
    """ Automatically creates user profiles for user instances """
    if created:
        Profile.objects.create(user=instance)