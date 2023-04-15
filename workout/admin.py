from django.contrib import admin

from .models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ["date", "time", "duration"]
    list_filter = ["date", "time", "duration"]
    search_fields = ["date", "time", "duration"]
