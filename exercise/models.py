from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Exercise(models.Model):
    """Exercise model"""

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("date",)
        
    def __str__(self):
        return self.name
    
