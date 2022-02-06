from django.urls import path
from .api.views import profile_tweet_history_view

urlpatterns = [path("api/<str:username>", profile_tweet_history_view)]
