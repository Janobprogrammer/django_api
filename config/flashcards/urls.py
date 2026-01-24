from django.urls import path
from .views import FlashCardView


urlpatterns = [
    path("flashcards/", FlashCardView.as_view(), name="flashcards")
]