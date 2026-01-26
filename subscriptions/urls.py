from django.urls import path, include
from .views import SubscriptionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionView, basename='subscription')

urlpatterns = [
    path("", include(router.urls)),
]