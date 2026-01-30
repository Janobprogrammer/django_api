from rest_framework import serializers
from .models import UserAchievement


class AchievementSerializer(serializers.ModelSerializer):
    achieved_at = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )

    class Meta:
        model = UserAchievement
        fields = (
            "user",
            "title",
            "description",
            "achieved_at",
        )
