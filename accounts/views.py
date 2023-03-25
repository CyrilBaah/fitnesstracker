from django.contrib.auth import authenticate, get_user_model
from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import (
    ChangePasswordSerializer,
    CustomUserSerializer,
    LoginSerializer,
    LogoutSerializer,
    RegisterationSerializer,
)

User = get_user_model()


class RegisterationAPIView(GenericAPIView):
    """Registeration API view"""

    permission_classes = (AllowAny,)
    serializer_class = RegisterationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        response = {
            "status": "success",
            "code": status.HTTP_201_CREATED,
            "message": "Registration successful",
            "data": data,
        }
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(response, status=status.HTTP_201_CREATED)


class LoginAPIView(GenericAPIView):
    """Login API view"""

    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        serializer = CustomUserSerializer(user)
        token = RefreshToken.for_user(user)
        data = serializer.data
        response = {
            "status": "success",
            "code": status.HTTP_200_OK,
            "message": "Login successful",
            "data": data,
        }
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(response, status=status.HTTP_200_OK)


class ChangePasswordView(UpdateAPIView):
    """Change password"""

    serializer_class = ChangePasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }
            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutAPIView(GenericAPIView):
    """Logout users."""

    serializer_class = LogoutSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            response = {
                "status": "success",
                "code": status.HTTP_205_RESET_CONTENT,
                "message": "Logout successfully",
                "data": [],
            }
            return Response(response, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
