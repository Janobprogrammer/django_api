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
    user_uuid = serializers.CharField(max_length=12, required=True)
