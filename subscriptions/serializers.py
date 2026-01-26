from rest_framework import serializers
from .models import SubscriptionHistory


class SubscriptionSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )
    end_date = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )
    class Meta:
        model = SubscriptionHistory
        fields = (
            "student",
            "teacher",
            "plan",
            "start_date",
            "end_date",
        )
