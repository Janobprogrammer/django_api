from rest_framework import generics, permissions
from .serializers import SubscriptionSerializer, SubscriptionHistory


class SubscriptionView(generics.CreateAPIView):
    queryset = SubscriptionHistory.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.AllowAny]