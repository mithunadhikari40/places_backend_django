from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from apps.user import views

router = DefaultRouter()

router.register('add_place', views.UserSavedPlacesView, basename='add_place')

urlpatterns = [
    # path('add_place', views.UserSavedPlacesView),
    path('', include(router.urls)),
    path('uploaded_places', views.user_uploaded_places),

    # path('add_place/<int:pk>', views.UserSavedPlacesView.as_view()),

]
