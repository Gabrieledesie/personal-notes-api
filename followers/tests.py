class FollowTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.follow_url = reverse("follow")
        self.unfollow_url = reverse("unfollow")

        self.user1 = {"username": "user1", "password": "pass1234"}
        self.user2 = {"username": "user2", "password": "pass1234"}

        self.client.post(self.register_url, self.user1)
        self.client.post(self.register_url, self.user2)
        login = self.client.post(self.login_url, self.user1)
        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_follow_user(self):
        response = self.client.post(self.follow_url, {"username": "user2"})
        self.assertEqual(response.status_code, 200)

    def test_unfollow_user(self):
        self.client.post(self.follow_url, {"username": "user2"})
        response = self.client.post(self.unfollow_url, {"username": "user2"})
        self.assertEqual(response.status_code, 200)
