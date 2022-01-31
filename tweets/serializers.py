from rest_framework import serializers

from .models import TweetModel

TWEET_ACTION_OPTIONS = ["like", "unlike", "retweet"]


class TweetSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TweetModel
        fields = ["id", "content", "likes"]

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, content):
        if len(content) > 300:
            raise serializers.ValidationError("This is too much sir")
        return content


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, action):
        action = action.lower().strip()
        if action not in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("Not a valid action for tweets")
        return action
