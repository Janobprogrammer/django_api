from django.urls import path, include
from .views import AdsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inter-ads', AdsView, basename='inter-ad')

urlpatterns = [
    path("", include(router.urls), name="inter-ad")
]