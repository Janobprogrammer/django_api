from rest_framework import serializers
from .models import FlashCard


class FlashCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlashCard
        fields = (
            "author",
            "title",
            "flash_type",
            "description",
            "words",
            "definition",
            "image",
        )
