from django.urls import path
from .views import (
    home_view,
    tweets_list_view,

)

urlpatterns = [
    path("", tweets_list_view),

