from rest_framework import permissions, viewsets
from .serializers import SubscriptionSerializer, SubscriptionHistory


class SubscriptionView(viewsets.ModelViewSet):
    queryset = SubscriptionHistory.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.AllowAny]