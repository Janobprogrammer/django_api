from .serializers import SteakSerializer
from rest_framework import permissions, viewsets
from .models import Steak


class SteakView(viewsets.ModelViewSet):
    queryset = Steak.objects.all()
    serializer_class = SteakSerializer
    permission_classes = [permissions.AllowAny]

