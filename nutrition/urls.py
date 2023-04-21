from django.urls import path

from . import views

urlpatterns = [
    path(
        "create-nutrition/", views.NutritionCreateView.as_view(), name="create-exercise"
    ),
    path("", views.NutritionListView.as_view(), name="create-exercise"),
    path("my-nutrition/", views.NutritionDetailView.as_view(), name="my-nutrition"),
    path(
        "update-nutrition/<int:pk>/",
        views.NutritionUpdateView.as_view(),
        name="update-nutrition",
    ),
    path(
        "delete-nutrition/<int:pk>/",
        views.NutritionDeleteView.as_view(),
        name="delete-nutrition",
    ),
]
