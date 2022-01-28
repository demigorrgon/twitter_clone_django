from django.db import models
from django.core.validators import MaxLengthValidator


class TweetModel(models.Model):
    content = models.TextField(
        validators=[MaxLengthValidator], max_length=300, blank=True, null=True
    )
    image = models.FileField(upload_to="images/", blank=True, null=True)

    def serialize(self):
        return {"id": self.id, "content": self.content, "likes": 42}
