from django.contrib import admin

from apps.favorites.models import FavoriteModel


class FavoriteAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        "user",
        "favorite",
        "created_at",
        "updated_at",
        "deleted_at",
    ]
    list_filter = ["favorite", "user"]
    # these are the fields that can be updated
    search_fields = ["name", "user"]
    ordering = ["favorite", "created_at"]
    model = FavoriteModel


admin.site.register(FavoriteModel, FavoriteAdmin)
