from rest_framework import serializers

from workout.models import Workout


class WorkoutSerializer(serializers.ModelSerializer):
    """Serializer for Workout."""

    class Meta:
        model = Workout
        fields = "__all__"
