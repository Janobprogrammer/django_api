from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.utils import timezone

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "uuid",
            "name",
            "surname", 
            "username", 
            "gender", 
            "birthday", 
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
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
        return obj.userachievement_set.values(
            "title",
            "description",
            "achieved_at",
        )

    @staticmethod
    def get_flashcards(obj):
        return obj.flashcards.values(
            "id",
            "title",
            "flash_type",
            "description",
            "words",
            "image",
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


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    uuid = serializers.CharField(write_only=True, required=True)
    phone_model = serializers.CharField(write_only=True, required=False)

    def validate(self, attrs: dict):
        email = attrs.get("email")
        password = attrs.get("password")
        device_uuid = attrs.get("uuid")
        phone_model = attrs.get("phone_model")

        if not device_uuid:
            raise serializers.ValidationError({
                "uuid": "Device UUID is required"
            })

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "email": "Invalid email address"
            })

        if not user.check_password(password):
            raise serializers.ValidationError({
                "password": "Invalid password"
            })

        if not user.is_active:
            raise serializers.ValidationError("User account is not active")

        if user.uuid and user.uuid != device_uuid:
            device_name = user.phone_model or "unknown device"
            last_login = (
                user.last_active.isoformat()
                if user.last_active
                else "unknown time"
            )

            raise serializers.ValidationError({
                "detail": "This account already has an active session on another device.",
                "phone_model": device_name,
                "last_login": last_login,
            })

        previous_login = user.last_active

        if not user.uuid:
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
    new_uuid = serializers.CharField()
    new_phone_model = serializers.CharField()

    def validate(self, attrs):
        user = self.context["request"].user

        if not user.uuid:
            raise serializers.ValidationError(
                "No active device found for this user"
            )

        if attrs["new_uuid"] == user.uuid:
            raise serializers.ValidationError(
                "The new device cannot be the same as the current device"
            )

        if User.objects.filter(uuid=attrs["new_uuid"]).exists():
            raise serializers.ValidationError(
                "This device is already linked to another account"
            )

        return attrs

    def save(self):
        user = self.context["request"].user
        old_phone = user.phone_model
        old_uuid = user.uuid

        user.uuid = self.validated_data["new_uuid"]
        user.phone_model = self.validated_data["new_phone_model"]
        user.last_active = timezone.now()
        user.save(update_fields=["uuid", "phone_model", "last_active"])

        return {
            "old_device": old_phone,
            "new_device": user.phone_model,
            "swapped_at": user.last_active,
            "old_uuid": old_uuid,
            "new_uuid": user.uuid,
        }
