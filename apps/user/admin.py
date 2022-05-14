from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from apps.user.models import UserSavedPlacesModel


class UserSavedPlacesAdmin(admin.ModelAdmin):
    list_display = [
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
        "created_at",
        "updated_at",
        "deleted_at",
    ]
    list_filter = ["name", "user"]
    # these are the fields that can be updated
    search_fields = ["name", "user"]
    ordering = ["name", "created_at"]
    model = UserSavedPlacesModel


admin.site.register(UserSavedPlacesModel, UserSavedPlacesAdmin)
