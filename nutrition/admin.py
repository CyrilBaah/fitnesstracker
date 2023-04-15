from django.contrib import admin

from .models import Nutrition


@admin.register(Nutrition)
class NutritionAdmin(admin.ModelAdmin):
    list_display = ["name", "food_type", "calorie_count", "date", "user"]
    list_filter = ["name", "food_type", "calorie_count"]
    search_fields = ["name", "food_type", "calorie_count"]
