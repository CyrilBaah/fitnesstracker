from django.conf import settings
from django.db import models


# Create your models here.
class Exercises(models.Model):
    """Exercise model"""

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user"
    )

    class Meta:
        ordering = ("date",)

    def __str__(self):
        return self.name
