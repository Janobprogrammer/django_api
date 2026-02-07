from rest_framework import serializers
from .models import Achievement, UserAchievedAt
from django.utils import timezone
from datetime import datetime


class AchievementMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = (
            "id",
            "title",
            "achievement_type",
            "description",
            "max_quantity",
            "icon",
        )


class AchievementSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(
        format="%d/%m/%Y",
        required=False,
        allow_null=True
    )
    icon = serializers.FileField(required=False)

    class Meta:
        model = Achievement
        fields = (
            "id",
            "title",
            "achievement_type",
            "description",
            "max_quantity",
            "icon",
            "created_at",
        )


class UserAchievedAtSerializer(serializers.ModelSerializer):
    achievement = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all()
    )
    achieved_at = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = UserAchievedAt
        fields = (
            "id",
            "achievement",
            "quantity",
            "achievements_date",
            "achieved_at",
        )

    def update(self, instance, validated_data):
        new_date = validated_data.get("achieved_at")

        if not new_date:
            new_date = timezone.now().strftime("%d/%m/%Y")

        try:
            datetime.strptime(new_date, "%d/%m/%Y")
        except ValueError:
            raise serializers.ValidationError({
                "achieved_at": "Noto'g'ri sana formati, dd/mm/yyyy bo'lishi kerak."
            })

        if not instance.achievements_date:
            instance.achievements_date = []

        instance.achievements_date.append(new_date)

        instance.quantity = min(instance.quantity + 1, instance.achievement.max_quantity)

        instance.save()
        return instance

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["achievement"] = AchievementSerializer(instance.achievement).data
        data["achievements_date"] = instance.achievements_date or []
        return data
