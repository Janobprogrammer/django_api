from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import RegisterAPIView, ProfileAPIView, CustomTokenObtainPairView

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
]
