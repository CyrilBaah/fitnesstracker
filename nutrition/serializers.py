from rest_framework import serializers

from nutrition.models import Nutrition


class NutritionSerializer(serializers.ModelSerializer):
    """Serializer for Nutritions."""

    class Meta:
        model = Nutrition
        fields = "__all__"
