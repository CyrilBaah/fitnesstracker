from rest_framework import serializers

from exercises.serializers import ExerciseSerializer
from workout.models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout."""

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = "__all__"

    def update(self, instance, validated_data):
        exercises_data = validated_data.pop("exercises", None)
        if exercises_data:
            # update exercises here
            pass
        return super().update(instance, validated_data)
