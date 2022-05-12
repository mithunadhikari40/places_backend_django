from django.db import models

from apps.user_auth.models import UserAuthModel
from apps.utils.timestamp.models import TimeStamp


class UserSavedPlacesModel(TimeStamp):
    user = models.ForeignKey(UserAuthModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    image = models.ImageField("images/")
    description = models.CharField(max_length=1024)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    address = models.CharField(max_length=512)
    monument = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)

    def __str__(self):
        return self.name
