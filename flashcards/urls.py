from django.urls import path, include
from .views import FlashCardView, WordListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'flash-cards', FlashCardView, basename='flash-card')
router.register(r'word-lists', WordListView, basename='word-list')

urlpatterns = [
    path("", include(router.urls)),
]