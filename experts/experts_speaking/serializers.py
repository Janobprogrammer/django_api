from rest_framework import serializers
from .models import (
    Topic,
    TopicQuestion,
    Answer,
    Idea,
    Vocabulary,
    SpeakingExam, SpeakingPart,
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
    answers = serializers.StringRelatedField(many=True, read_only=True)
    ideas = serializers.StringRelatedField(many=True, read_only=True)
    vocabularies = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = TopicQuestion
        fields = ['id', 'question', 'answers', 'ideas', 'vocabularies']


class SpeakingTopicSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = SpeakingPart
        fields = ['id', 'title', 'part', 'questions']

    def get_questions(self, obj):
        return SpeakingQuestionSerializer(obj.topic.questions.all(), many=True).data


class SpeakingExamSerializer(serializers.ModelSerializer):
    part1 = SpeakingTopicSerializer(read_only=True)
    part2 = SpeakingTopicSerializer(read_only=True)
    part3 = SpeakingTopicSerializer(read_only=True)

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
