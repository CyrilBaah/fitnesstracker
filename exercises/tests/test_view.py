from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


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

    # def test_create_exercise(self):
    #     url = reverse("create-exercise")
    #     data = {
    #         "name": "New Exercise",
    #         "type": "Cardio",
    #         "description": "This is a new exercise",
    #     }
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, 201)
    #     self.assertEqual(Exercises.objects.count(), 2)
    
    # def test_create_exercise(self):
    #     url = reverse('create-exercise')
    #     data = {
    #         'name': 'New Exercise',
    #         'type': 'Cardio',
    #         'description': 'This is a new exercise',
    #         'user': self.user,
    #     }
    #     self.client.force_authenticate(user=self.user)
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Exercises.objects.count(), 1)
    #     exercise = Exercises.objects.get()
    #     self.assertEqual(exercise.name, 'New Exercise')
    #     self.assertEqual(exercise.type, 'Cardio')
    #     self.assertEqual(exercise.description, 'This is a new exercise')
    #     self.assertEqual(exercise.user, self.user)

    # def test_update_exercise(self):
    #     url = reverse('exercise-detail', args=[self.exercise.id])
    #     data = {
    #         'name': 'Updated Exercise',
    #         'type': 'Cardio',
    #         'description': 'This is an updated exercise',
    #     }
    #     response = self.client.patch(url, data)
    #     self.assertEqual(response.status_code, 200)
    #     self.exercise.refresh_from_db()
    #     self.assertEqual(self.exercise.name, 'Updated Exercise')
    #     self.assertEqual(self.exercise.type, 'Cardio')
    #     self.assertEqual(self.exercise.description, 'This is an updated exercise')

    # def test_delete_exercise(self):
    #     url = reverse('exercise-detail', args=[self.exercise.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, 204)
    #     self.assertFalse(Exercises.objects.filter(id=self.exercise.id).exists())
