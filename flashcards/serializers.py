from rest_framework import serializers
from .models import FlashCard, WordList


class WordListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WordList
        fields = (
            "id",
            "word",
            "definition",
            "image",
        )


class FlashCardSerializer(serializers.ModelSerializer):
    word_list = serializers.SerializerMethodField()

    class Meta:
        model = FlashCard
        fields = (
            "author",
            "title",
            "flash_type",
            "description",
            "word_list",
        )

    def get_word_list(self, obj: WordList):
        parts = obj.flash_cards.all().order_by("id")
        return WordListSerializer(parts, many=True).data