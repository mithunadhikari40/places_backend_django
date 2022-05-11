from django.contrib import admin

from .models import UserAuthModel
from rest_framework_simplejwt.tokens import RefreshToken


def get_token_for_user(user: UserAuthModel) -> dict:
    refresh_token = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh_token),
        'access_token': str(refresh_token.access_token)
    }
