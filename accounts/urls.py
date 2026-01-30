from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterAPIView, ProfileAPIView, CustomTokenObtainPairView, LogoutView, DeviceSwapAPIView,
    PasswordResetConfirmAPIView, PasswordResetRequestAPIView, PasswordUpdateAPIView, UUIDCheckAPIView,
    DeleteAccountAPIView, UserDetailAPIView, UserSearchAPIView
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("logout/", LogoutView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("profile/", ProfileAPIView.as_view()),
    path("device/swap/", DeviceSwapAPIView.as_view()),
    path("password-reset/otp-request/", PasswordResetRequestAPIView.as_view()),
    path("password-reset/otp-confirm/", PasswordResetConfirmAPIView.as_view()),
    path("password-reset/new-password-confirm/", PasswordUpdateAPIView.as_view()),
    path("check-uuid/", UUIDCheckAPIView.as_view()),
    path("delete/", DeleteAccountAPIView.as_view()),
    path("users/<int:id>/", UserDetailAPIView.as_view(), name="user-detail"),
    path("search/<str:username>/", UserSearchAPIView.as_view(), name="search-by-username"),
]
