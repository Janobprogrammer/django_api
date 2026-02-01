import hashlib
import random
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import PasswordResetOTP
from config import settings

User = get_user_model()


def generate_public_id(email: str) -> str | None:
    if len(email) < 8:
        return None
    if "@" not in email:
        return None
    base = email.split("@")[0].lower()
    salt = settings.SECRET_KEY
    rnd = random.randint(1000, 9999)

    raw = f"{base}{rnd}{salt}"
    return hashlib.sha256(raw.encode()).hexdigest()[:8]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email", "password", "uuid", "name",
            "surname", "username", "gender", "birthday",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)

        for _ in range(10):
            code = generate_public_id(user.email)
            if code and not User.objects.filter(user_uuid=code.upper()).exists():
                user.user_uuid = code.upper()
                break

        if not user.user_uuid:
            raise serializers.ValidationError("user_uuid could not be generated")

        user.set_password(password)
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    steaks = serializers.SerializerMethodField()
    achievements = serializers.SerializerMethodField()
    flashcards = serializers.SerializerMethodField()
    friends = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()
    subscriptions = serializers.SerializerMethodField()

    birthday = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )

    class Meta:
        model = User

        fields = (
            "id",
            "uuid",
            "username",
            "name",
            "surname",
            "email",
            "role",
            "birthday",
            "balance",
            "points",

            "gender",
            "avatar",
            "phone_model",
            "steaks_count",
            "likes",

            # Social
            "instagram",
            "telegram",
            "youtube",

            # IELTS BANDS
            "speaking_band",
            "reading_band",
            "listening_band",
            "writing_band",

            "rating",
            "rating_count",
            "reward",
            "user_uuid",
            "date_joined",
            "premium",

            "trf_number",
            "trf_date",

            "last_active",

            # FKs
            "friends",
            "steaks",
            "achievements",
            "flashcards",
            "followers",
            "following",
            "subscriptions",
        )

    @staticmethod
    def get_friends(obj):
        return obj.user.values(
            "friend",
        )

    @staticmethod
    def get_steaks(obj):
        return obj.steaks.values(
            "date",
            "is_active",
        )

    @staticmethod
    def get_achievements(obj):
        return [
            {
                "id": item.achievement.id,
                "title": item.achievement.title,
                "achievement_type": item.achievement.achievement_type,
                "description": item.achievement.description,
                "max_quantity": item.achievement.max_quantity,
                "icon": item.achievement.icon.url if item.achievement.icon else None,
                "quantity": item.quantity,  # 👈 MANA SHU
                "achievements_date": item.achievements_date,
            }
            for item in obj.achieved_user.select_related("achievement")
        ]

    @staticmethod
    def get_flashcards(obj):
        return obj.flashcards.values(
            "id",
            "author",
            "title",
            "flash_type",
            "description",
        )

    @staticmethod
    def get_followers(obj):
        return obj.followers.select_related("follower").values(
            "follower__id",
        )

    @staticmethod
    def get_following(obj):
        return obj.following.select_related("following").values(
            "following__id",
        )

    @staticmethod
    def get_subscriptions(obj):
        return obj.subscriptions.select_related("teacher").values(
            "teacher__id",
            "start_date",
            "end_date",
        )


class OneUserSerializer(serializers.ModelSerializer):
    birthday = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )

    class Meta:
        model = User

        fields = (
            "id",
            "uuid",
            "username",
            "name",
            "surname",
            "email",
            "role",
            "birthday",
            "balance",
            "points",

            "gender",
            "avatar",
            "phone_model",
            "steaks_count",
            "likes",

            # Social
            "instagram",
            "telegram",
            "youtube",

            # IELTS BANDS
            "speaking_band",
            "reading_band",
            "listening_band",
            "writing_band",

            "rating",
            "rating_count",
            "reward",
            "date_joined",
            "premium",
            "trf_number",
            "trf_date",
            "last_active",
        )


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    uuid = serializers.CharField(write_only=True, required=True)
    phone_model = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        device_uuid = attrs.get("uuid")
        phone_model = attrs.get("phone_model")

        # print(f"Tokens: {attrs = }")

        if not device_uuid:
            print(f"raise {device_uuid = }")
            raise serializers.ValidationError({"uuid": "Device UUID is required"})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print("User not found")
            raise serializers.ValidationError({"email": "Invalid email address"})

        if not user.check_password(password):
            print("Wrong password")
            raise serializers.ValidationError({"password": "Invalid password"})

        if not user.is_active:
            print("User is passive")
            raise serializers.ValidationError("User account is not active")

        old_user = (
            User.objects
            .filter(uuid=device_uuid)
            .exclude(id=user.id)
            .first()
        )

        if old_user:
            old_user.uuid = None
            old_user.phone_model = None
            old_user.last_active = None
            old_user.save(update_fields=["uuid", "phone_model", "last_active"])

        if user.uuid and user.uuid != device_uuid:
            print("This account already has an active session on another device.", device_uuid)
            raise serializers.ValidationError({
                "detail": "This account already has an active session on another device.",
                "phone_model": user.phone_model or "unknown device",
                "last_login": user.last_active.isoformat() if user.last_active else None
            })

        previous_login = user.last_active

        user.uuid = device_uuid
        if phone_model:
            user.phone_model = phone_model

        user.last_active = timezone.now()
        user.save(update_fields=["uuid", "phone_model", "last_active"])

        data = super().validate(attrs)

        data["phone_model"] = user.phone_model
        data["previous_login"] = previous_login
        data["current_login"] = user.last_active

        return data


class DeviceSwapSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    uuid = serializers.CharField()
    phone_model = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        new_uuid = attrs.get("uuid")
        new_phone_model = attrs.get("phone_model")
        print("=" * 20)
        print(f"{email = }\n{password = }\n{new_uuid = }\n{new_phone_model = }")
        print("=" * 20)

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid email or password")

        if new_uuid == user.uuid:
            raise serializers.ValidationError("The new device cannot be the same as the current device")

        if User.objects.filter(uuid=new_uuid).exists():
            raise serializers.ValidationError("This device is already linked to another account")

        attrs["user"] = user
        return attrs

    def save(self):
        try:
            user = self.validated_data["user"]
            old_phone = user.phone_model
            old_uuid = user.uuid

            user.uuid = self.validated_data["uuid"]
            user.phone_model = self.validated_data["phone_model"]
            user.last_active = timezone.now()
            user.save(update_fields=["uuid", "phone_model", "last_active"])

            refresh = RefreshToken.for_user(user)

            return {
                "old_device": old_phone,
                "new_device": user.phone_model,
                "swapped_at": user.last_active,
                "old_uuid": old_uuid,
                "new_uuid": user.uuid,

                "tokens": {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            }
        except (Exception, ValueError) as err:
            return {
                "status_code": 500,
                "response": str(err)
            }


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, val: str):
        if not User.objects.filter(email=val).exists():
            raise serializers.ValidationError("User not found")
        return val


class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=6)

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
            otp = PasswordResetOTP.objects.get(user=user, code=attrs["code"])
        except (User.DoesNotExist, PasswordResetOTP.DoesNotExist):
            raise serializers.ValidationError("Invalid code or email")

        if otp is None:
            raise serializers.ValidationError("Invalid OTP code")

        if otp.is_expired():
            otp.delete()
            raise serializers.ValidationError("OTP expired")

        attrs["user"] = user
        attrs["otp"] = otp
        return attrs


class PasswordUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    new_password = serializers.CharField(max_length=32, min_length=8)

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs["email"])
            passw = attrs["new_password"]
            user.set_password(passw)
            user.save(update_fields=["password"])
        except (Exception, User.DoesNotExist):
            raise serializers.ValidationError("Invalid email or user not found")
        return attrs


class UUIDCheckSerializer(serializers.Serializer):
    uuid = serializers.CharField(max_length=100)

    def validate_uuid(self, value):
        if not User.objects.filter(uuid=value).exists():
            raise serializers.ValidationError("UUID not found")
        return value
