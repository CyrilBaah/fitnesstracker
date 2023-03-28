from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path(
        "create-exercise/", views.ExerciseCreateView.as_view(), name="create-exercise"
    ),
]
