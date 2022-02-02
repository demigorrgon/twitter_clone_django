from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import TweetModel


class TweetsTestCase(TestCase):
    User = get_user_model()

    def setUp(self):
        self.User.objects.create(username="somebody", password="somepassword")
        self.User.objects.create(username="someone", password="somepassword")
        self.User.objects.create(username="someone_else", password="somepassword")

    def test_user_created(self):
        user = self.User.objects.get(username="somebody")
        self.assertEqual(user.username, "somebody")
