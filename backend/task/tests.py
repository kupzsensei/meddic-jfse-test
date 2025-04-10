from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from task.models import Task, Category
from task.serializers import TaskReadSerializer


class TaskViewsTestCase(APITestCase):
    def setUp(self):
        # Create a default user for testing
        self.user = User.objects.create_user(username="user1", password="password123")
        
        # Authenticate the user
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Create a category for testing
        self.category = Category.objects.create(name="Work", user=self.user)
        
        # Create a task for testing
        self.task = Task.objects.create(
            name="Test Task",
            description="This is a test task.",
            category=self.category,
            completed=False,
            priority=False,
            user=self.user
        )

    def test_create_task(self):
        """Test creating a new task."""
        url = reverse('task-list-create')  # Use reverse to generate the URL
        data = {
            "name": "New Task",
            "description": "This is a new task.",
            "category": self.category.id,
            "completed": False,
            "priority": False
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "New Task")

    def test_retrieve_task(self):
        """Test retrieving a task by ID."""
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.id})  # Use reverse with kwargs
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.task.name)

    def test_update_task(self):
        """Test updating an existing task."""
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.id})  # Use reverse with kwargs
        data = {
            "name": "Updated Task",
            "description": "This task has been updated.",
            "category": self.category.id,
            "completed": True,
            "priority": False
        }
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Task")
        self.assertTrue(response.data["completed"])

    def test_delete_task(self):
        """Test deleting a task."""
        url = reverse('task-retrieve-update-destroy', kwargs={'pk': self.task.id})  # Use reverse with kwargs
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
