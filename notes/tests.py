from django.urls import reverse
from rest_framework.test import APITestCase, APIClient

class NotesTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.notes_url = reverse("notes-list")
        self.refresh_url = reverse("token_refresh")
        self.user_data = {"username": "noteuser", "password": "pass1234"}
        self.client.post(self.register_url, self.user_data)
        login = self.client.post(self.login_url, self.user_data)
        token = login.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + token)

    def test_register_user(self):
        data = {"username": "newuser", "password": "newpass123"}
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        response = self.client.post(self.login_url, self.user_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_refresh_token(self):
        login = self.client.post(self.login_url, self.user_data)
        refresh = login.data["refresh"]
        response = self.client.post(self.refresh_url, {"refresh": refresh})
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)

    def test_create_note(self):
        data = {"title": "My Note", "content": "This is a test note"}
        response = self.client.post(self.notes_url, data)
        self.assertEqual(response.status_code, 201)

    def test_read_notes(self):
        response = self.client.get(self.notes_url)
        self.assertEqual(response.status_code, 200)

    def test_update_note(self):
        note = self.client.post(self.notes_url, {"title": "Old", "content": "Old content"}).data
        note_url = reverse("notes-detail", args=[note["id"]])
        response = self.client.put(note_url, {"title": "New", "content": "New content"})
        self.assertEqual(response.status_code, 200)

    def test_delete_note(self):
        note = self.client.post(self.notes_url, {"title": "Delete", "content": "To delete"}).data
        note_url = reverse("notes-detail", args=[note["id"]])
        response = self.client.delete(note_url)
        self.assertEqual(response.status_code, 204)
