from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserAuthModel


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = UserAuthModel
        fields = ("email", "password")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserAuthModel
        fields = ("email", "password")


from django.contrib.auth.admin import UserAdmin


class UserAuthAdmin(UserAdmin):
    # class UserAuthAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'password',
        'registration_date',
        'is_staff',
        'is_superuser',
        'deleted_at',
        'push_token'
    ]
    list_filter = ['email', 'is_superuser']
    # these are the fields that can be updated
    fieldsets = ((None, {"fields": ("phone", "name", "push_token", "password")}),)
    # these are the fields that are asked when registering
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("name", "phone", "email", "password1", "password2", "push_token")}),)
    search_fields = ("email", "is_superuser")
    ordering = ("email",)
    model = UserAuthModel


admin.site.register(UserAuthModel, UserAuthAdmin)
