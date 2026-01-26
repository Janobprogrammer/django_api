from rest_framework import permissions, viewsets
from .serializers import FriendListSerializer
from .models import FriendList


class FriendListView(viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer
    permission_classes = [permissions.AllowAny]
