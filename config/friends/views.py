from rest_framework import generics, permissions
from .serializers import FriendListSerializer
from .models import FriendList


class FriendListView(generics.CreateAPIView):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer
    permission_classes = [permissions.AllowAny]
