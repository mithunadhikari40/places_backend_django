from django.contrib import admin

from .models import UserAuthModel, UserSavedPlacesModel

from .models import UserAuthModel
from rest_framework import serializers


class UserSavedPlacesSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=512)
    image = serializers.ImageField()
    description = serializers.CharField(max_length=1024)
    city = serializers.CharField(max_length=50)
    street = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=512)
    monument = serializers.CharField(max_length=100)
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

    def validate_image(self, value):
        length = len(value)
        if length < 8:
            raise serializers.ValidationError("Image must be at least 8 characters long.")

        return value

    """Object level validation, Its syntax will be validate. We can access all the data in the second parameter
           We either raise an validation error or return that object, we can access the object in second parameter"""

    def validate(self, data):
        return data

    class Meta:
        model = UserSavedPlacesModel
        fields = [
            'id',
            "user",
            "name",
            "image",
            "description",
            "city",
            "street",
            "address",
            "monument",
            "latitude",
            "longitude",
        ]
