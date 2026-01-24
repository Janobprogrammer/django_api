from rest_framework import generics, permissions
from .serializers import FollowingSerializer
from .models import Follow


class FollowingView(generics.CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [permissions.AllowAny]