from django.urls import path
from .views import AchievementView


urlpatterns = [
    path("achievements/", AchievementView.as_view(), name="achievements"),
]