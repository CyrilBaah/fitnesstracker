from django.urls import include, path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path("register/", views.RegisterationAPIView.as_view(), name="create-user"),
    # path("login/", views.LoginAPIView.as_view(), name="login-user"),
    # path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    # path("logout/", views.UserLogoutAPIView.as_view(), name="logout-user"),
]
