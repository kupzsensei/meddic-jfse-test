from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from core.serializers import RegisterSerializer


class RegisterViewTests(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')  # Ensure you have a URL pattern named 'register'
        self.valid_user_data = {
            "username": "testusercase",
            "password": "Password123!",
            "password_confirm": "Password123!"
        }
        self.invalid_user_data = {
            "username": "",
            "password": "short",
            "password_confirm": "short"
        }

    def test_register_user_with_valid_data(self):
        response = self.client.post(self.register_url, self.valid_user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username="testusercase").exists())

    def test_register_user_with_invalid_data(self):
        response = self.client.post(self.register_url, self.invalid_user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(User.objects.filter(username="").exists())

    def test_register_user_with_existing_username(self):
        User.objects.create_user(username="testusercase", password="Password123!")
        response = self.client.post(self.register_url, self.valid_user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.filter(username="testusercase").count(), 1)



class RegisterSerializerTestCase(APITestCase):
    def test_valid_data_creates_user(self):
        data = {
            "username": "testuser",
            "password": "securepassword123",
            "password_confirm": "securepassword123"
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, data["username"])
        self.assertTrue(user.check_password(data["password"]))

    def test_passwords_do_not_match(self):
        data = {
            "username": "testuser",
            "password": "securepassword123",
            "password_confirm": "differentpassword123"
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)
        self.assertEqual(serializer.errors["password_confirm"][0],"Passwords do not match")

    def test_missing_password_confirm(self):
        data = {
            "username": "testuser",
            "password": "securepassword123"
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    def test_missing_username(self):
        data = {
            "password": "securepassword123",
            "password_confirm": "securepassword123"
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

