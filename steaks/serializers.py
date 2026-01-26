from rest_framework import serializers
from .models import Steak


class SteakSerializer(serializers.ModelSerializer):
    date = serializers.DateField(
        format="%d/%m/%Y",
        input_formats=["%d/%m/%Y"],
        required=False,
        allow_null=True
    )
    class Meta:
        model = Steak
        fields = (
            "user",
            "date",
            "is_active",
        )

