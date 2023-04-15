from rest_framework import serializers

from exercises.serializers import ExerciseSerializer
from workout.models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout."""

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = "__all__"
