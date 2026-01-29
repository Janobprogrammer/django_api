import random
from django.db import transaction
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model, logout, update_session_auth_hash
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import PasswordResetOTP, PasswordResetOTPHistory
from .serializers import (
    RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer, DeviceSwapSerializer,
    PasswordResetRequestSerializer, PasswordResetConfirmSerializer, PasswordUpdateSerializer, UUIDCheckSerializer
)
from rest_framework.views import APIView

User = get_user_model()

MAX_DAILY_ATTEMPTS: int = 5


def check_daily_limit(user: User) -> bool:
    today = timezone.now().date()

    attempts = PasswordResetOTPHistory.objects.filter(
        user=user,
        created_at__date=today
    ).count()

    return attempts < MAX_DAILY_ATTEMPTS


def generate_otp():
    return str(random.randint(100000, 999999))


@method_decorator(csrf_exempt, name="dispatch")
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        user = request.user

        user.uuid = None
        user.phone_model = None
        user.last_active = None
        user.save(update_fields=["uuid", "phone_model", "last_active"])

        logout(request)

        return Response(
            data={
            "detail": "Logged out successfully. You can now log in from another device."
            }
        )


class DeviceSwapAPIView(generics.CreateAPIView):
    serializer_class = DeviceSwapSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = DeviceSwapSerializer(
            data=request.data,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.save()

        return Response(
            {
                "detail": (
                    f"Device successfully switched: "
                    f"{data['old_device']} → {data['new_device']}"
                ),
                "data": data
            },
            status=status.HTTP_200_OK
        )


class PasswordResetRequestAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetRequestSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data["email"])

        if not check_daily_limit(user):
            return Response(
                {
                    "detail": "You have exceeded the daily limit. Try again tomorrow."
                },
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        PasswordResetOTP.objects.filter(user=user).delete()

        code = generate_otp()
        PasswordResetOTP.objects.create(user=user, code=code)
        PasswordResetOTPHistory.objects.create(user=user, code=code)

        user.email_user(
            subject="Password Reset Code From InterIELTS Application",
            message=f"Your password reset code: {code}"
        )

        return Response(
            {"detail": "OTP sent to email"},
            status=status.HTTP_200_OK
        )


class PasswordResetConfirmAPIView(generics.CreateAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        otp = serializer.validated_data["otp"]
        otp.delete()
        return Response(
            {"detail": "Successful"},
            status=status.HTTP_200_OK
        )


class PasswordUpdateAPIView(generics.CreateAPIView):
    serializer_class = PasswordUpdateSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = PasswordUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data["email"])
        update_session_auth_hash(request, user)
        return Response(
            {"detail": "Successful"},
            status=status.HTTP_200_OK
        )


class UUIDCheckAPIView(generics.CreateAPIView):
    serializer_class = UUIDCheckSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UUIDCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            {
                "exists": True,
                "uuid": serializer.validated_data["uuid"]
            },
            status=status.HTTP_200_OK
        )


class DeleteAccountAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        user = request.user

        with transaction.atomic():
            user.uuid = None
            user.phone_model = None
            user.last_active = None
            user.save(update_fields=["uuid", "phone_model", "last_active"])

            try:
                from rest_framework_simplejwt.token_blacklist.models import (
                    OutstandingToken, BlacklistedToken
                )
            except (Exception, ValueError):
                pass

            user.delete()

        return Response(
            {"detail": "Account successfully deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
