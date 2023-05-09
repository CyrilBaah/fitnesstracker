from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from exercises.models import Exercises


class ExerciseTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpass", email="testemail@email.com"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.exercise = Exercises.objects.create(
            name="Test Exercise",
            type="Strength Training",
            description="This is a test exercise",
            user=self.user,
        )

    def test_get_exercise_list(self):
        url = reverse("my-exercises")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.exercise.name)
