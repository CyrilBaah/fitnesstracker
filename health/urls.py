from django.urls import path

from .views import HealthCheck

urlpatterns = [
    path("", HealthCheck.as_view(), name="health_check"),
]
