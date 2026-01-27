from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, permissions, status
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout
from .serializers import RegisterSerializer, UserSerializer, CustomTokenObtainPairSerializer, DeviceSwapSerializer
from rest_framework.views import APIView

User = get_user_model()


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
