from rest_framework import serializers
from .models import (
    Topic,
    TopicQuestion,
    Answer,
    Idea,
    Vocabulary,
    SpeakingExam,
)


class SpeakingVocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'


class SpeakingIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class SpeakingAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class SpeakingQuestionSerializer(serializers.ModelSerializer):
    answers = SpeakingAnswerSerializer(many=True)
    ideas = SpeakingIdeaSerializer(many=True)
    vocabularies = SpeakingVocabularySerializer(many=True)

    class Meta:
        model = TopicQuestion
        fields = '__all__'


class SpeakingTopicSerializer(serializers.ModelSerializer):
    questions = SpeakingQuestionSerializer(many=True)

    class Meta:
        model = Topic
        fields = '__all__'


class SpeakingExamSerializer(serializers.ModelSerializer):
    part1 = SpeakingTopicSerializer(many=True, read_only=True)
    part2 = SpeakingTopicSerializer(many=True, read_only=True)
    part3 = SpeakingTopicSerializer(many=True, read_only=True)

    class Meta:
        model = SpeakingExam
        fields = '__all__'


class SpeakingExamWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingExam
        fields = (
            'id',
            'name',
            'is_active',
            'part1',
            'part2',
            'part3',
        )
