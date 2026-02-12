from datetime import timedelta
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import permissions, viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import FriendListSerializer, AddFriendListSerializer
from .models import FriendList

User = get_user_model()


class FriendListAPIView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendListSerializer

    def get_queryset(self):
        return FriendList.objects.filter(user=self.request.user)


class AddFriendAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddFriendListSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_uuid = serializer.validated_data["user_uuid"]
        user = request.user

        if FriendList.objects.filter(friend=user).exists():
            return Response(
                {"detail": "You already added a referral before"},
                status=400
            )

        try:
            friend = User.objects.get(user_uuid=user_uuid)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        if friend == user:
            return Response({"detail": "You cannot add yourself"}, status=400)

        if timezone.now() - user.date_joined > timedelta(hours=24):
            return Response(
                {"detail": "Referral expired after 24 hours"},
                status=400
            )

        FriendList.objects.create(
            user=friend,
            friend=user
        )

        return Response(
            {"detail": "Referral successfully added"},
            status=201
        )
