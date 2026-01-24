from rest_framework import generics, permissions
from .serializers import FlashCardSerializer
from .models import FlashCard


class FlashCardView(generics.CreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [permissions.AllowAny]
