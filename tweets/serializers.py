from rest_framework import serializers

from .models import TweetModel

TWEET_ACTION_OPTIONS = ["like", "unlike", "retweet"]


class TweetCreateSerializer(serializers.ModelSerializer):
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


class TweetSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    # content = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)
    # is_retweet = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = TweetModel
        fields = ["id", "username", "content", "likes", "is_retweet", "parent"]

    def get_username(self, obj):
        return obj.user.username

    def get_likes(self, obj):
        return obj.likes.count()

    # def get_content(self, obj):
    #     content = obj.content
    #     if obj.is_retweet():
    #         content = obj.parent.content
    #     return content


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    # content = serializers.CharField(allow_blank=True, required=False)

    def validate_action(self, action):
        action = action.lower().strip()
        if action not in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("Not a valid action for tweets")
        return action
