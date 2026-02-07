from rest_framework import viewsets, permissions
from django.db import transaction
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Achievement, UserAchievedAt
from .serializers import AchievementSerializer, UserAchievedAtSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class AchievementView(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]


class UserAchievedAtView(viewsets.ModelViewSet):
    queryset = UserAchievedAt.objects.all()
    serializer_class = UserAchievedAtSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return UserAchievedAt.objects.filter(user=self.request.user)

    @transaction.atomic
    def perform_create(self, serializer):
        achievement = serializer.validated_data["achievement"]

        obj, created = UserAchievedAt.objects.select_for_update().get_or_create(
            user=self.request.user,
            achievement=achievement,
            defaults={
                "quantity": 0,
                "achievements_date": [timezone.now().strftime("%d/%m/%Y")],
            }
        )

        if obj.quantity >= achievement.max_quantity:
            raise ValidationError(
                {"achievement": "Max quantity ga yetilgan"}
            )

        # POST qilganda ham quantity oshadi va bugungi sana qo'shiladi
        obj.quantity = min(obj.quantity + 1, obj.achievement.max_quantity)
        if not obj.achievements_date:
            obj.achievements_date = []
        obj.achievements_date.append(timezone.now().strftime("%d/%m/%Y"))
        obj.save()

        serializer.instance = obj
