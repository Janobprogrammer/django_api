from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from .models import (
    Question, Answer, Idea, Vocabulary, Topic
)
from .serializers import (
    Part1QuestionSerializer, Part1TopicSerializer, Part1IdeaSerializer, Part1VocabularySerializer,
    Part1AnswerSerializer,
)


class Part1QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Part1QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class Part1AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = Part1AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class Part1IdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = Part1IdeaSerializer
    permission_classes = [permissions.IsAuthenticated]


class Part1VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = Part1VocabularySerializer
    permission_classes = [permissions.IsAuthenticated]


class Part1TopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'part_1_questions__part_1_answers',
        'part_1_questions__part_1_ideas',
        'part_1_questions__part_1_vocabularies'
    )
    serializer_class = Part1TopicSerializer
    permission_classes = [permissions.IsAuthenticated]
