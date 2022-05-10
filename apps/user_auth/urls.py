from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

"""Viewset"""
from rest_framework.routers import DefaultRouter

from apps.user_auth import views

# creating a router object
router = DefaultRouter()
# register student viewset with router
# model view set
# router.register('register', views.RegisterApi, basename='register')

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.RegisterApi.as_view()),

]
