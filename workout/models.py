# Create your models here.
from django.conf import settings
from django.db import models

from exercises.models import Exercises


# Create your models here.
class Workout(models.Model):
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()
    exercises = models.ManyToManyField(Exercises, related_name="workout", blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="workout"
    )

    def __str__(self):
        return str(self.date)
