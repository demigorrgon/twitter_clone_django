from django.urls import path
from .views import (
    tweet_view,
    tweet_action_view,
    tweets_list_view,
    tweets_list_json,
    tweet_create_view,
    tweet_delete_view,
)

urlpatterns = [
    path("", tweets_list_view),
    path("tweets/", tweets_list_json),
    path("tweets/<int:tweet_id>", tweet_view),
    path("tweets/create", tweet_create_view),
    path("tweets/<int:tweet_id>/delete", tweet_delete_view),
    path("tweets/action", tweet_action_view),
]
