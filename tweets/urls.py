from django.urls import path
from .views import tweets_list_view


urlpatterns = [
    path("", tweets_list_view),
]
