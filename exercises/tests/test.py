from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Exercises


class ExercisesModelTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )
        self.exercise = Exercises.objects.create(
            name="Test Exercise",
            type="Strength Training",
            description="This is a test exercise",
            user=self.user,
        )

    def test_exercise_name(self):
        self.assertEqual(str(self.exercise), "Test Exercise")

    def test_exercise_type(self):
        self.assertEqual(self.exercise.type, "Strength Training")

    def test_exercise_description(self):
        self.assertEqual(self.exercise.description, "This is a test exercise")

    def test_exercise_date(self):
        self.assertEqual(self.exercise.date, date.today())

    def test_exercise_user(self):
        self.assertEqual(self.exercise.user, self.user)

    def test_exercise_ordering(self):
        exercise2 = Exercises.objects.create(
            name="Test Exercise 2",
            type="Cardio",
            description="This is another test exercise",
            user=self.user,
        )
        exercises = Exercises.objects.all()
        self.assertEqual(exercises[0], self.exercise)
        self.assertEqual(exercises[1], exercise2)
