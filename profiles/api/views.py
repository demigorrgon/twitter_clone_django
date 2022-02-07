from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from tweets.models import TweetModel
from tweets.serializers import TweetSerializer
from profiles.models import ProfileModel
from profiles.serializers import PublicProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

User = get_user_model()


@api_view(["GET"])
def profile_tweet_history_view(request, username, *args, **kwargs):
    get_object_or_404(User, username=username)
    queryset = TweetModel.objects.filter(user__username=username)
    tweets = TweetSerializer(queryset, many=True)

    return Response(tweets.data)


@api_view(["GET", "POST"])
def profile_follow_by_current_user_view(request, username, *args, **kwargs):
    print(username)
    profile_user_object = get_object_or_404(ProfileModel, user__username=username)
    # print(profile_user_object)
    data = request.data
    if request.method == "POST":
        current_user = request.user
        # xmlhttprequest
        action = data.get("action")
        if profile_user_object != current_user:
            if action == "follow":
                profile_user_object.followers.add(current_user)
            elif action == "unfollow":
                profile_user_object.followers.remove(current_user)

    serializer = PublicProfileSerializer(
        instance=profile_user_object, context={"request": request}
    )
    print(serializer.data)
    return Response(serializer.data)
