import random
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model, logout, update_session_auth_hash
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import PasswordResetOTP
from .serializers import (
    RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer, DeviceSwapSerializer,
    PasswordResetRequestSerializer, PasswordResetConfirmSerializer, PasswordUpdateSerializer
)
from rest_framework.views import APIView

User = get_user_model()


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

    def post(self, request):
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

    def post(self, request):
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

    def post(self, request: Request):
        serializer = PasswordResetRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=serializer.validated_data["email"])

        PasswordResetOTP.objects.filter(user=user).delete()

        code = generate_otp()
        PasswordResetOTP.objects.create(user=user, code=code)

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

    def post(self, request):
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
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        user = request.user
        serializer = PasswordUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        update_session_auth_hash(request, user)
        return Response(
            {"detail": "Successful"},
            status=status.HTTP_200_OK
        )
