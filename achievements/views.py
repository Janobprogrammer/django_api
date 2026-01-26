from rest_framework import permissions
from .serializers import AchievementSerializer
from .models import UserAchievement
from rest_framework import viewsets


class AchievementView(viewsets.ModelViewSet):
    queryset = UserAchievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.AllowAny]
