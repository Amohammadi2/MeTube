from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    profile_img = models.ImageField(upload_to="/profiles/", null=True, blank=True)
    bio = models.CharField(max_length=200)


class Channel(models.Model):
    subscribers = models.ManyToManyField(User, through=u"Subscription", related_name="subscriptions")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)


class Video(models.Model):
    channel = models.ForeignKey(Channel)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    video = models.FileField(upload_to="/videos/")
    poster = models.ImageField(upload_to="/imgs/")

class Comment(models.Model):
    # both User and Video models have access to
    # the comments through their `comments` property
    commenter = models.ForeignKey(User, related_name="comments")
    video = models.ForeignKey(Video, related_name="comments")
    comment_text = models.CharField(max_length=300)

class Notification(models.Model):
    status_choices = [
        ("e", "error"),
        ("i", "info"),
        ("s", "success"),
    ]

    text = models.CharField(max_length=300)
    status = models.CharField(choices = Notification.status_choices)
    seen = models.BooleanField(default=True)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return  self.status + self.text


class Subscription(models.Model):
    subscriber = models.ForeignKey(User)
    subscribed_channel = models.ForeignKey(Channel)
    subscription_date = models.DateField()
    receive_notifications = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # if the this is not an `update` process
        # then automatically set the subscription date
        # to the current time of the system
        if not self.id:
            self.subscription_date = now().date
        return super().save(*args, **kwargs)