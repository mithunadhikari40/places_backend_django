from apps.user.models import UserSavedPlacesModel
from apps.user_auth.models import UserAuthModel
from apps.utils.timestamp.models import TimeStamp
from django.db import models


class FavoriteModel(TimeStamp):
    user = models.ForeignKey(UserAuthModel, on_delete=models.CASCADE)
    favorite = models.ForeignKey(UserSavedPlacesModel, on_delete=models.CASCADE)
