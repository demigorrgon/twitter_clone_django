from django.db import models


class TweetModel(models.Model):
    content = models.TextField(max_length=300, blank=True, null=True)
    image = models.FileField(upload_to="images/", blank=True, null=True)
