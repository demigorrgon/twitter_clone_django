from django.db import models
from django.contrib.auth import get_user_model
from tweets.models import TweetModel

# Create your models here.

User = get_user_model()


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)
    # tweet_history = models.ManyToManyField(TweetModel, related_name="tweets")
