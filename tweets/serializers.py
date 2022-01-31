from rest_framework import serializers

from .models import TweetModel


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = ["content"]

    def validate_content(self, content):
        if len(content) > 300:
            raise serializers.ValidationError("This is too much sir")
        return content
