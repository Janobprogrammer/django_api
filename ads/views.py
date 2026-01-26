from rest_framework import permissions, viewsets
from .models import InterAds
from .serializers import AdsSerializer


class AdsView(viewsets.ModelViewSet):
    queryset = InterAds.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [permissions.AllowAny]
