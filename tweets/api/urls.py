from django.urls import path
from .views import (
    tweet_view,
    tweet_feed_view,
    tweet_action_view,
    tweets_list_json,
    tweet_create_view,
    tweet_delete_view,
)

"""
ENDPOINT: /api/tweets/
"""
urlpatterns = [
    path("", tweets_list_json),
    path("feed/", tweet_feed_view),
    path("<int:tweet_id>/", tweet_view),
    path("create/", tweet_create_view),
    path("<int:tweet_id>/delete/", tweet_delete_view),
    path("action/", tweet_action_view),
]
