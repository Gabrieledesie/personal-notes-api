from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")  # your user registration endpoint
        self.login_url = reverse("token_obtain_pair")
        self.refresh_url = reverse("token_refresh")
        self.user = {
            "username": "edesie",
            "email": "edesie@example.com",
            "password": "StrongPassword123"
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user)
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.login_url, {
            "username": "edesie",
            "password": "StrongPassword123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_token(self):
        self.client.post(self.register_url, self.user)
        login = self.client.post(self.login_url, {
            "username": "edesie",
            "password": "StrongPassword123"
        })
        refresh = login.data["refresh"]
        response = self.client.post(self.refresh_url, {"refresh": refresh})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
