from rest_framework import permissions, viewsets
from .serializers import FollowingSerializer
from .models import Follow


class FollowingView(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowingSerializer
    permission_classes = [permissions.IsAuthenticated]
