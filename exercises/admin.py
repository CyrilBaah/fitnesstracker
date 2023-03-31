from django.contrib import admin

from .models import Exercises


@admin.register(Exercises)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "description", "date", "user"]
    list_filter = ["name", "type", "date"]
    search_fields = ["name", "type", "description"]
