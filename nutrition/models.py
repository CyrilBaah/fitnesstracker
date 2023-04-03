from django.conf import settings
from django.db import models


# Create your models here.
class Nutrition(models.Model):
    FOOD_TYPE_CHOICES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]
    name = models.CharField(max_length=200)
    food_type = models.CharField(max_length=20, choices=FOOD_TYPE_CHOICES)
    calorie_count = models.PositiveIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="nutritions"
    )
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.calorie_count} cal)"

    class Meta:
        ordering = ["-date"]
