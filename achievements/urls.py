from django.urls import path, include
from .views import AchievementView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'achievements', AchievementView, basename='achievement')

urlpatterns = [
    path("", include(router.urls)),
]