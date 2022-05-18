from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.favorites import views

router = DefaultRouter()

router.register('', views.FavoriteView, basename='')

urlpatterns = [
    # path('add_place', views.UserSavedPlacesView),
    path('', include(router.urls))

    # path('add_place/<int:pk>', views.UserSavedPlacesView.as_view()),

]
