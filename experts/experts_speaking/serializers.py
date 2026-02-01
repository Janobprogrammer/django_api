from rest_framework import serializers
from .models import (
    Question, Answer, Idea, Vocabulary, Topic,
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
    audio = serializers.FileField(required=False)

    class Meta:
        model = Answer
        fields = '__all__'

    def get_queryset(self):
        return Answer.objects.filter(teacher__role="teacher")

    def create(self, validated_data):
        user = self.context["request"].user

        if user.role != "teacher":
            raise serializers.ValidationError("Only teachers can answer")

        validated_data["teacher"] = user
        return super().create(validated_data)


class SpeakingQuestionSerializer(serializers.ModelSerializer):
    answers = serializers.StringRelatedField(many=True, read_only=True)
    ideas = serializers.StringRelatedField(many=True, read_only=True)
    vocabularies = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'answers', 'ideas', 'vocabularies']


class SpeakingTopicSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = [
            'id',
            'title',
            'part',
            'topic_type',
            'main_question',
            'questions',
        ]

    def get_questions(self, obj):
        qs = obj.questions.all().order_by("id")
        if obj.part == "part2":
            subquestions = list(qs.values_list("question", flat=True))
            return {
                "main_question": obj.main_question,
                "subquestions": subquestions if subquestions else []
            }
        return SpeakingQuestionSerializer(qs, many=True).data
