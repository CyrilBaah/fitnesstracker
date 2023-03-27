from django.conf import settings
from rest_framework import serializers

from exercises.models import Exercises


class ExerciseSerializer(serializers.ModelSerializer):
    """Serializer for Exercise"""

    # user = serializers.PrimaryKeyRelatedField(
    #     queryset=settings.AUTH_USER_MODEL.objects.all()
    # )

    class Meta:
        model = Exercises
        fields = "__all__"
        # fields = ("name", "type", "description", "date")
