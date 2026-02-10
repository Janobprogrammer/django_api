from rest_framework import serializers
from accounts.serializers import FriendSerializer
from .models import FriendList


class FriendListSerializer(serializers.ModelSerializer):
    friend = FriendSerializer(read_only=True)

    class Meta:
        model = FriendList
        fields = ("friend",)


class AddFriendListSerializer(serializers.Serializer):
    user_uuid = serializers.CharField(max_length=100, required=True)

    class Meta:
        fields = ("user_uuid",)
