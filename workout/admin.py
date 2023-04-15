from django.contrib import admin

from .models import Workout


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = [
        "date",
        "time",
        "duration",
    ]
    list_filter = ["date", "time", "duration"]
    search_fields = ["date", "time", "duration"]


# from django.contrib import admin
# from django.utils.text import format_lazy
# from django.utils.html import format_html_join
# from django.urls import reverse
# from .models import Workout


# class WorkoutAdmin(admin.ModelAdmin):
#     list_display = ["date", "time", "duration", "display_exercises"]
#     list_filter = ["date", "time", "duration"]
#     search_fields = ["date", "time", "duration", "exercises__name"]

#     def display_exercises(self, obj):
#         return format_html_join(
#             ", ",
#             "<a href='{url}'>{name}</a>",
#             (
#                 (reverse("admin:exercises_exercises_change", args=(exercise.id,)), exercise.name)
#                 for exercise in obj.exercises.all()
#             ),
#         )
#     display_exercises.short_description = "Exercises"

# admin.site.register(Workout, WorkoutAdmin)
