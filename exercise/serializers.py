from rest_framework import serializers

from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise"""

    class Meta:
        model = Exercise
        fields = "__all__"
        # fields = ("name", "type", "description", "date")
