from django.urls import path

from . import views

urlpatterns = [
    path(
        "create-exercise/", views.ExerciseCreateView.as_view(), name="create-exercise"
    ),
    path("", views.ExerciseListView.as_view(), name="list-exercises"),
    path("my-exercises/", views.ExerciseDetailView.as_view(), name="my-exercises"),
    path(
        "update-exercise/<int:pk>/",
        views.ExerciseUpdateView.as_view(),
        name="update-exercises",
    ),
    path(
        "delete-exercise/<int:pk>/",
        views.ExerciseDeleteView.as_view(),
        name="delete-exercises",
    ),
]
