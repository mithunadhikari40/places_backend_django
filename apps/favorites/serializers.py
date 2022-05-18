from rest_framework import serializers

from apps.favorites.models import FavoriteModel
from apps.user.serializers import UserSavedPlacesSerializer
from apps.user_auth.serializers import UserAuthSerializer


class FavoriteSerializer(serializers.ModelSerializer):
    # favorite = UserSavedPlacesSerializer()
    # user = UserAuthSerializer()

    class Meta:
        model = FavoriteModel
        fields = ['id', 'user', 'favorite']
