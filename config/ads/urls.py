from django.urls import path
from .views import AdsView

urlpatterns = [
    path("inter-ads/", AdsView.as_view(), name="inter-ads")
]