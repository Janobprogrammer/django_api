from rest_framework import permissions, viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import FlashCardSerializer, WordListSerializer
from .models import FlashCard, WordList


class FlashCardView(viewsets.ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    permission_classes = [permissions.IsAuthenticated]


class WordListView(viewsets.ModelViewSet):
    queryset = WordList.objects.all()
    serializer_class = WordListSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
