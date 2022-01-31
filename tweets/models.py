from django.db import models
from django.contrib.auth import get_user_model


class TweetLikeModel(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("TweetModel", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class TweetModel(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name="tweet_user", blank=True, null=True, through=TweetLikeModel
    )
    content = models.TextField(max_length=300, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # image = models.FileField(upload_to="images/", blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    # def __str__(self):
    #     return self.content

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": 42}
