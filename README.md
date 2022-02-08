# twitter_clone_django
twitter-like app for learning using ```django```, ```Django Rest Framework```, Bootstrap and vanilla js based on https://www.youtube.com/watch?v=f1R_bykXHGE&t=16683s and [Learn Django 3 by example](https://www.amazon.com/Django-Example-powerful-reliable-applications/dp/1838981950)

 - All views are function-based

 - DRF's ```serializers``` are used to serialize django model

 - Django signal in ```profiles.models``` is used to create ```ProfileModel``` for current user after registration 

TODO: Practice with class based views in DRF

[![codecov](https://codecov.io/gh/demigorrgon/twitter_clone_django/branch/main/graph/badge.svg?token=9ESNX8YOVN)](https://codecov.io/gh/demigorrgon/twitter_clone_django)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Available functionality of:

- Users:
    - Registration
    - Login
    - Logout
    - History of tweets and retweeting in profile

TODO: add form to edit profile, option to see followers and whomst is followed

- Permissions:
    - Tweeting only as logged in user
    - Deleting/liking/following/retweeting only as logged in user

TODO: add some js shenanigans to distinguish between own tweets and retweets in templates

- Pagination of API with ```paginator``` of ```django_rest_framework```

TODO: add proper processing for pagination on client side.

TODO: MOAR TESTS
