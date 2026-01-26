from django.urls import path, include
from .views import SteakView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'steaks', SteakView, basename='steak')

urlpatterns = [
    path("", include(router.urls)),
]