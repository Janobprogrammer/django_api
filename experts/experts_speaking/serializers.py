from rest_framework import serializers
from .models import (
    Question, Answer, Idea, Vocabulary, SpeakingExam, SpeakingPart, SpeakingPartName, Topic,
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
    speaking_topic = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = ['id', 'title', 'topic_type', 'speaking_topic', 'questions']

    def get_questions(self, obj):
        qs = obj.questions.all().order_by('id')
        questions = list(qs.values_list('question', flat=True))
        return questions

    def get_speaking_topic(self, obj):
        parts = obj.speaking_topic.all().order_by("id")
        return SpeakingPartSerializer(parts, many=True).data


class SpeakingPartSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    part_names = serializers.SerializerMethodField()

    class Meta:
        model = SpeakingPart
        fields = ['id', 'title', 'part', 'main_question', 'questions', 'part_names']

    def get_questions(self, obj):
        qs = obj.topic.questions.all().order_by('id')
        if obj.part == "part2":
            subquestions = list(qs.values_list('question', flat=True))
            all_subquestions = subquestions
            return {
                "main_question": obj.main_question,
                "subquestions": all_subquestions if all_subquestions else None
            }

        return SpeakingQuestionSerializer(qs, many=True).data

    def get_part_names(self, obj):
        if obj.part == "part2":
            part_names = list(obj.part_names.values_list('topic_name', flat=True))
            return part_names
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.part != "part2":
            data.pop("part_names", None)
            data.pop("main_question", None)

        return data


class SpeakingExamSerializer(serializers.ModelSerializer):
    part1 = SpeakingPartSerializer(read_only=True)
    part2 = SpeakingPartSerializer(read_only=True)
    part3 = SpeakingPartSerializer(read_only=True)

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


class SpeakingPartNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakingPartName
        fields = (
            'id',
            'name',
        )

