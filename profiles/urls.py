from django.urls import path
from .api.views import profile_tweet_history_view, profile_follow_by_current_user_view

"""
endpoint: api/profiles/
"""
urlpatterns = [
    path("<str:username>", profile_tweet_history_view),
    path("<str:username>/follow/", profile_follow_by_current_user_view),
]
