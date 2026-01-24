from rest_framework import serializers
from .models import InterAds


class AdsSerializer(serializers.ModelSerializer):
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
        model = InterAds
        fields = (
            "title",
            "text",
            "ad_type",
            "link",
            "start_date",
            "end_date",
            "duration",
            "views",
            "image",
        )
