from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .views import (
    RegisterAPIView, ProfileAPIView, CustomTokenObtainPairView, LogoutView, DeviceSwapAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("device/swap/", DeviceSwapAPIView.as_view()),
]
