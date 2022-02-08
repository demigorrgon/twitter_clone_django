from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from .models import TweetModel


class TweetsTestCase(TestCase):
    User = get_user_model()

    def setUp(self):
        self.user = self.User.objects.create(
            username="somebody", password="somepassword"
        )
        self.user_someone = self.User.objects.create(
            username="someone", password="somepassword"
        )
        self.user_someone_else = self.User.objects.create(
            username="someone_else", password="somepassword"
        )
        TweetModel.objects.create(content="wasdakek", user=self.user)
        TweetModel.objects.create(content="idk", user=self.user_someone)
        TweetModel.objects.create(content="out of ideas", user=self.user_someone_else)

    def get_client(self):
        client = APIClient()
        client.login(username="somebody", password="somepassword")
        # client.force_authenticate()
        return client

    def test_user_created(self):
        user = self.User.objects.get(username="somebody")
        self.assertEqual(user.username, "somebody")

    def test_tweet_created(self):
        tweet = TweetModel.objects.create(content="wasda", user=self.user)
        self.assertEqual(self.user.id, 1)
        self.assertEqual(tweet.user, self.user)

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_tweet_create_view(self):
        client = self.get_client()
        client.force_authenticate(user=self.user)
        response = client.post(
            "/api/tweets/create/",
            data={"content": "testing stuff"},
        )
        self.assertEqual(response.status_code, 201)

    def test_action_like(self):
        client = self.get_client()
        client.force_login(user=self.user)
        response = client.post("/api/tweets/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)

    def test_action_unlike(self):
        client = self.get_client()
        client.force_login(user=self.user)
        response = client.post("/api/tweets/action/", {"id": 1, "action": "like"})
        self.assertEqual(response.status_code, 200)
        response = client.post("/api/tweets/action/", {"id": 1, "action": "unlike"})
        self.assertEqual(response.status_code, 200)
        like_count = response.json().get("likes")
        self.assertEqual(like_count, 0)

    def test_action_retweet(self):
        client = self.get_client()
        client.force_login(user=self.user)
        response = client.post("/api/tweets/action/", {"id": 2, "action": "retweet"})
        self.assertEqual(response.status_code, 201)
        data = response.json()
        new_tweet_id = data.get("id")
        self.assertNotEqual(new_tweet_id, 2)

    def test_tweet_detail_api_view(self):
        client = self.get_client()
        response = client.get("/api/tweets/1/")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        _id = data.get("id")
        self.assertEqual(_id, 1)

    def test_tweet_delete_api_view(self):
        client = self.get_client()
        client.force_login(user=self.user)
        response = client.post(
            "/api/tweets/create/",
            data={"content": "testing stuff"},
        )
        self.assertEqual(response.status_code, 201)
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 200)
        # client = self.get_client()
        # client.force_login(user=self.user)
        response = client.delete("/api/tweets/1/delete/")
        self.assertEqual(response.status_code, 404)
        response_incorrect_owner = client.delete("/api/tweets/3/delete/")
        self.assertEqual(
            response_incorrect_owner.status_code, 200
        )  # force login -> 200
