from django.urls import path

from . import views

urlpatterns = [
    path("create-workout/", views.WorkoutCreateView.as_view(), name="create-workout"),
    path("", views.WorkoutListView.as_view(), name="create-workout"),
    path("my-workout/", views.WorkoutDetailView.as_view(), name="my-workout"),
    path(
        "update-workout/<int:pk>/",
        views.WorkoutUpdateView.as_view(),
        name="update-workout",
    ),
    path(
        "delete-workout/<int:pk>/",
        views.WorkoutDeleteView.as_view(),
        name="delete-workout",
    ),
]
