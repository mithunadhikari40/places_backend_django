"""places URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt import views as jwt_views

from config import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # for the docs
                  path('schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),

                  # default auth route and other rest_framework routes
                  path('auth/', include('rest_framework.urls', namespace="rest_framework")),
                  path('api/auth/', include('apps.user_auth.urls'), name="auth"),
                  path('api/user/', include('apps.user.urls'), name="user"),
                  path('api/favorite/', include('apps.favorites.urls'), name="favorites"),
                  path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
