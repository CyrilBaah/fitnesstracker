from rest_framework import serializers

from workout.models import Workout
from exercises.serializers import ExerciseSerializer


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout."""
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = "__all__"
