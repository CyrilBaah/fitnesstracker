import secrets

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """CustomUser Serializer"""

    class Meta:
        model = CustomUser
        fields = ("id", "username", "email")


class RegisterationSerializer(serializers.ModelSerializer):
    """Registration Serializer"""

    class Meta:
        model = CustomUser

        # Temporary remove Google ID Docs
        # fields = ("id", "username", "email", "password", "google_id")

        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True, "required": False}}

    # def create(self, validated_data):
    #     return CustomUser.objects.create_user(**validated_data)

    def create(self, validated_data):
        # Check if google_id is present in the validated data
        if "google_id" in validated_data:
            # If so, create a Google user
            password = secrets.token_urlsafe(32)
            return CustomUser.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                google_id=validated_data["google_id"],
                password=password,
            )
        else:
            # Otherwise, create a normal user
            return CustomUser.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
                password=validated_data["password"],
            )


# class LoginSerializer(serializers.Serializer):
#     """Login Serializer"""
#     email = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Incorrect Credentials")


class LoginSerializer(serializers.Serializer):
    """Login Serializer"""

    email = serializers.CharField()
    password = serializers.CharField(write_only=True, required=False)
    # google_id = serializers.CharField(required=False) # Temporary remove Google ID Docs

    def validate(self, data):
        # Check if a password was provided
        if "password" in data:
            user = authenticate(**data)
            if user and user.is_active:
                return user
        else:
            # If no password was provided, try to authenticate using Google ID
            try:
                user = CustomUser.objects.get(
                    email=data["email"], google_id__isnull=False
                )
                if user and user.is_active:
                    return user
            except CustomUser.DoesNotExist:
                pass
        raise serializers.ValidationError("Incorrect Credentials")


class ChangePasswordSerializer(serializers.Serializer):
    """Change password Serializer"""

    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class LogoutSerializer(serializers.Serializer):
    """Logout Serializer"""

    refresh = serializers.CharField()
    default_error_message = {"bad_token": ("Token is expired or invalid")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")
