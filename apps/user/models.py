from django.db import models

from apps.user_auth.models import UserAuthModel
from apps.utils.timestamp.models import TimeStamp


class UserSavedPlacesModel(TimeStamp):
    def upload_to(self, filename):
        return f'images/{filename}'.format(filename=filename)

    user = models.ForeignKey(UserAuthModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    image = models.ImageField("images/", upload_to=upload_to)
    description = models.CharField(max_length=1024)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    address = models.CharField(max_length=512)
    monument = models.CharField(max_length=100)
    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)

    def __str__(self):
        return f"{self.name}-{self.image}"
