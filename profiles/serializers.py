from rest_framework import serializers

# from tweets.models import TweetModel
from django.contrib.auth import get_user_model

User = get_user_model()


class UserProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    parent_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    content = serializers.CharField(max_length=300)
    # class Meta:
    # fields = ["id", "parent_id", "user_id", "content"]
