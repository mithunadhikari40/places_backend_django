from django.contrib import admin

from .models import UserAuthModel


class UserAuthAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'registration_date',
        'is_admin',
        'push_token'
    ]


admin.site.register(UserAuthModel, UserAuthAdmin)
