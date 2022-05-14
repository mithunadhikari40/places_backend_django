from rest_framework_simplejwt.tokens import RefreshToken

from apps.user_auth.models import UserAuthModel


def get_token_for_user(user: UserAuthModel) -> dict:
    refresh_token = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh_token),
        'access_token': str(refresh_token.access_token)
    }


def get_random_string_with_datetime() -> str:
    from datetime import datetime
    import string
    import random

    now = datetime.now()
    time_str = str(now).replace(" ", "")
    length = 10  # number of characters in the string.
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return ran + time_str
