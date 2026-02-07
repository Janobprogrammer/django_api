from django.utils import timezone
from rest_framework import serializers
from .models import FriendList


class FriendListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendList
        fields = (
            "user",
            "friend",
        )


class AddFriendSerializer(serializers.Serializer):
    user_uuid = serializers.CharField(max_length=100, required=True)

    def validate(self, attrs):
        return attrs
