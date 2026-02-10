from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FriendListAPIView, AddFriendAPIView

router = DefaultRouter()
router.register(r'friends', FriendListAPIView, basename='friend')

urlpatterns = [
    path("", include(router.urls)),
    path("add-friend/", AddFriendAPIView.as_view()),
]