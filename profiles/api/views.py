from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from tweets.models import TweetModel
from tweets.serializers import TweetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()


@api_view(["GET"])
def profile_tweet_history_view(request, username, *args, **kwargs):
    get_object_or_404(User, username=username)
    queryset = TweetModel.objects.filter(user__username=username)
    tweets = TweetSerializer(queryset, many=True)

    return Response(tweets.data)
