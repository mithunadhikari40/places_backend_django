from django.forms import ModelForm
from .models import UserSavedPlacesModel


class UserSavedPlacesForm(ModelForm):
    class Meta:
        model = UserSavedPlacesModel
        fields = [
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
        exclude = ["user"]
