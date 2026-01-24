from .serializers import SteakSerializer
from rest_framework import generics, permissions
from .models import Steak


class SteakView(generics.CreateAPIView):
    queryset = Steak.objects.all()
    serializer_class = SteakSerializer
    permission_classes = [permissions.AllowAny]

