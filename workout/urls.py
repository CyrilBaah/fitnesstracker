from django.urls import path

from . import views

urlpatterns = [
    path("create-workout/", views.WorkoutCreateView.as_view(), name="create-workout"),
]
