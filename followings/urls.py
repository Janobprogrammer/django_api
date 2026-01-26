from django.urls import path, include
from .views import FollowingView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'followings', FollowingView, basename='following')

urlpatterns = [
    path("", include(router.urls)),
]