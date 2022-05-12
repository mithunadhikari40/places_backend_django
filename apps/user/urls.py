from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from apps.user import views

urlpatterns = [
    path('add_place', views.UserSavedPlacesView.as_view()),

]
