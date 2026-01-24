from rest_framework import generics, permissions
from .models import InterAds
from .serializers import AdsSerializer


class AdsView(generics.CreateAPIView):
    queryset = InterAds.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [permissions.AllowAny]
