from django.urls import path, include
from .views import FlashCardView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flash-cards', FlashCardView, basename='flash-card')

urlpatterns = [
    path("", include(router.urls)),
]