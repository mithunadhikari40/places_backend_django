from django.db import models
from ..utils.timestamp.models import TimeStamp


class UserAuthModel(TimeStamp):
    name = models.CharField(null=False, blank=False,max_length=512)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.FloatField(max_length=11)
    password = models.CharField(max_length=512)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    push_token = models.CharField(null=True,blank=True, max_length=1024)

    def __str__(self):
        return self.name
