from django.urls import path

from . import views

urlpatterns = [
    path("create-workout/", views.WorkoutCreateView.as_view(), name="create-workout"),
    path("", views.WorkoutListView.as_view(), name="create-workout"),
    path("my-workout/", views.WorkoutDetailView.as_view(), name="my-workout"),
    
]