from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

# Create your models here.

User = get_user_model()


class FollowerRelation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey("ProfileModel", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=220, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    followers = models.ManyToManyField(User, related_name="following", blank=True)
    # tweet_history = models.ManyToManyField(TweetModel, related_name="tweets")


def user_did_save(sender, instance, created, *args, **kwargs):
    if created:
        ProfileModel.objects.get_or_create(user=instance)


post_save.connect(user_did_save, sender=User)
