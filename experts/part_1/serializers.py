import re
from rest_framework import serializers
from .models import (
    Question, Answer, Idea, Vocabulary, Topic, TopicType,
)


class Part1TopicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicType
        fields = ("id", "name")


class Part1VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = '__all__'


class Part1IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'


class Part1AnswerSerializer(serializers.ModelSerializer):
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


class Part1QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    ideas = serializers.SerializerMethodField()
    vocabularies = serializers.SerializerMethodField()
    audio = serializers.FileField(required=False)

    class Meta:
        model = Question
        fields = ['id', 'topic', 'audio', 'question', 'answers', 'ideas', 'vocabularies']

    def get_answers(self, obj):
        qs = obj.part_1_answers.all().order_by("id")
        return Part1AnswerSerializer(qs, many=True).data

    def get_ideas(self, obj):
        qs = obj.part_1_ideas.all()
        return Part1IdeaSerializer(qs, many=True).data

    def get_vocabularies(self, obj):
        qs = obj.part_1_vocabularies.all()
        return Part1VocabularySerializer(qs, many=True).data


class Part1TopicSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    topic_type = Part1TopicTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = (
            'id',
            'title',
            'topic_type',
            'questions',
            'from_date',
            'to_date',
            'always_in_use'
        )

    def validate(self, attrs):
        from_date = attrs.get("from_date")
        to_date = attrs.get("to_date")
        always = attrs.get("always_in_use")

        pattern = r"^(0[1-9]|1[0-2])\.\d{4}$"

        if always:
            attrs["from_date"] = None
            attrs["to_date"] = None
            return attrs

        if from_date or to_date:
            if not (from_date and to_date):
                raise serializers.ValidationError(
                    "Both from_date and to_date must be provided"
                )

            if not re.match(pattern, from_date) or not re.match(pattern, to_date):
                raise serializers.ValidationError(
                    "Dates must be in format mm.yyyy"
                )

        return attrs

    def get_questions(self, obj):
        qs = obj.part_1_questions.all()
        return Part1QuestionSerializer(qs, many=True).data
