from rest_framework import permissions, viewsets
from .serializers import FlashCardSerializer
from .models import FlashCard


class FlashCardView(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [permissions.AllowAny]
