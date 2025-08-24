from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.refresh_url = reverse("token_refresh")

    def test_register_user(self):
        data = {"username": "testuser", "password": "pass1234"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post(self.register_url, {"username": "testuser", "password": "pass1234"})
        response = self.client.post(self.login_url, {"username": "testuser", "password": "pass1234"})
        self.assertEqual(response.status_code, 200)

    def test_refresh_token(self):
        self.client.post(self.register_url, {"username": "testuser", "password": "pass1234"})
        login = self.client.post(self.login_url, {"username": "testuser", "password": "pass1234"})
        refresh = login.data["refresh"]
        response = self.client.post(self.refresh_url, {"refresh": refresh})
        self.assertEqual(response.status_code, 200)
