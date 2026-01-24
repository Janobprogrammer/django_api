from rest_framework import generics, permissions
from .serializers import AchievementSerializer
from .models import UserAchievement


class AchievementView(generics.CreateAPIView):
    queryset = UserAchievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.AllowAny]
