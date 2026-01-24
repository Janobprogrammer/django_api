from django.urls import path
from .views import SteakView


urlpatterns = [
    path("steak-view/", SteakView.as_view(), name="steak-view"),
]