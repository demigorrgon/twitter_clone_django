from django.urls import path
from .views import (
    tweet_view,
    tweet_action_view,
    tweets_list_view,
    tweets_list_json,
    tweet_create_view,
    tweet_delete_view,
)

"""
api/tweets/
"""
urlpatterns = [
    path("", tweets_list_view),
    # path("tweets/", tweets_list_json),
    # path("tweets/<int:tweet_id>/", tweet_view),
    # path("tweets/create/", tweet_create_view),
    # path("tweets/<int:tweet_id>/delete/", tweet_delete_view),
    # path("tweets/action/", tweet_action_view),
    # path("", tweet_list_view),
    # path("feed/", tweet_feed_view),
    path("action/", tweet_action_view),
    path("create/", tweet_create_view),
    path("<int:tweet_id>/", tweet_view),
    path("<int:tweet_id>/delete/", tweet_delete_view),
]
