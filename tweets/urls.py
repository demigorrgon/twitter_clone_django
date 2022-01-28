from django.urls import path
from .views import tweet_view, tweets_list_view, tweets_list_json

urlpatterns = [
    path("", tweets_list_view),
    path("tweets/", tweets_list_json),
    path("tweets/<int:tweet_id>", tweet_view),
]
