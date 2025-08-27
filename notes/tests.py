from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class NotesTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("token_obtain_pair")
        self.notes_url = reverse("notes-list")  # Ensure your router in notes/urls.py uses basename='notes'
        self.user = {
            "username": "edesie",
            "email": "edesie@example.com",
            "password": "StrongPassword123"
        }

        self.client.post(self.register_url, self.user)
        login = self.client.post(self.login_url, {
            "username": "edesie",
            "password": "StrongPassword123"
        })
        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_create_note(self):
        response = self.client.post(self.notes_url, {"title": "Test", "content": "Content"})
        self.assertEqual(response.status_code, 201)

    def test_read_notes(self):
        response = self.client.get(self.notes_url)
        self.assertEqual(response.status_code, 200)
