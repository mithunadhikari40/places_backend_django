from django.db import models

from apps.user_auth.models import UserAuthModel
from apps.utils.timestamp.models import TimeStamp
from apps.utils.timestamp.utils import get_random_string_with_datetime


def upload_to(related_name, filename):
    print(f"The args are {filename} and other one is {related_name}")
    ext = filename.split(".")[-1]
    name = get_random_string_with_datetime()
    return f'places/images/{name}.{ext}'


class UserSavedPlacesModel(TimeStamp):
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
        return f"{self.name}-{self.id}"
