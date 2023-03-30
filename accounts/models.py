from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext as _
from django_rest_passwordreset.signals import reset_password_token_created

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    """Model representing a custom user"""

    email = models.EmailField(_("email address"), unique=True)
    google_id = models.CharField(_("google id"), max_length=100, unique=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


@receiver(reset_password_token_created)
def password_reset_token_created(
    sender, instance, reset_password_token, *args, **kwargs
):
    email_plaintext_message = "{}?token={}".format(
        reverse("password_reset:reset-password-request"), reset_password_token.key
    )

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email],
    )
