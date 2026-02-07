from rest_framework import serializers
from .models import (
    Topic, Question, Answer, Idea, Vocabulary, TopicName, TopicType,
)


class Part2TopicTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicType
        fields = ("id", "name")


class Part2VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = "__all__"


class Part2IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = "__all__"


class Part2AnswerSerializer(serializers.ModelSerializer):
    audio = serializers.FileField(required=False)

    class Meta:
        model = Answer
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        if user.role != "teacher":
            raise serializers.ValidationError("Only teachers can answer")
        validated_data["teacher"] = user
        return super().create(validated_data)


class Part2QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    ideas = serializers.SerializerMethodField()
    vocabularies = serializers.SerializerMethodField()
    audio = serializers.FileField(required=False)

    class Meta:
        model = Question
        fields = ("id", 'topic', 'audio', "question", "answers", "ideas", "vocabularies")

    def get_answers(self, obj):
        qs = Answer.objects.filter(question=obj.topic)
        return Part2AnswerSerializer(qs, many=True).data

    def get_ideas(self, obj):
        qs = obj.part_2_ideas.all()
        return Part2IdeaSerializer(qs, many=True).data

    def get_vocabularies(self, obj):
        qs = obj.part_2_vocabularies.all()
        return Part2VocabularySerializer(qs, many=True).data

class Part3NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ("id", "title")

class Part2TopicNameSerializer(serializers.ModelSerializer):
    part3_name = Part3NameSerializer(read_only=True)

    class Meta:
        model = TopicName
        fields = ("id", "part3_name")

class Part2TopicSerializer(serializers.ModelSerializer):
    subquestions = serializers.SerializerMethodField()
    part_names = serializers.SerializerMethodField()
    answers = serializers.SerializerMethodField()
    ideas = serializers.SerializerMethodField()
    vocabularies = serializers.SerializerMethodField()
    topic_type = Part2TopicTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Topic
        fields = (
            "id", "title", "topic_type", "question",
            "part_names", "always_in_use",
            "from_date", "to_date",
            "subquestions",
            "answers", "ideas", "vocabularies"
        )

    def get_subquestions(self, obj):
        return list(obj.part_2_questions.values_list("question", flat=True))

    def get_part_names(self, obj):
        return Part2TopicNameSerializer(obj.part_2_names.all(), many=True).data

    def get_answers(self, obj):
        return Part2AnswerSerializer(obj.part_2_answers.all(), many=True).data

    def get_ideas(self, obj):
        return Part2IdeaSerializer(obj.part_2_ideas.all(), many=True).data

    def get_vocabularies(self, obj):
        return Part2VocabularySerializer(obj.part_2_vocabularies.all(), many=True).data
