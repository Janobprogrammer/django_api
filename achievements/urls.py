from django.urls import path, include
from .views import AchievementView, UserAchievedAtView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'achievements', AchievementView, basename='achievement')
router.register(r'achieved-at', UserAchievedAtView, basename='achieved-at')

urlpatterns = [
    path("", include(router.urls)),
]