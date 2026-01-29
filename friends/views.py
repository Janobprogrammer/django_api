from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import FriendListSerializer, AddFriendSerializer
from .models import FriendList

User = get_user_model()


class FriendListView(viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer
    permission_classes = [permissions.IsAuthenticated]


class AddFriendAPIView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AddFriendSerializer

    def post(self, request: Request):
        serializer = AddFriendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_uuid = request.data.get("user_uuid")

        print(f"{user_uuid = }")

        if not user_uuid:
            return Response(
                data={"detail": "user_uuid not found"},
                status=400
            )

        try:
            friend = User.objects.get(user_uuid=user_uuid)
        except User.DoesNotExist:
            return Response(
                data={"detail": "User not found"},
                status=404
            )

        if friend == request.user:
            return Response(
                data={"detail": "You cannot add yourself as a friend."},
                status=400
            )

        obj, created = FriendList.objects.get_or_create(
            user=request.user,
            friend=friend
        )

        if not created:
            return Response(
                data={"detail": "This user is already on your friends list."},
                status=400
            )

        return Response(
            data={"detail": "User added to friends list"},
            status=201
        )

