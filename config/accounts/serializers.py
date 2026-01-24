from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "email",
            "password",
            "uuid",
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
            "count",
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
