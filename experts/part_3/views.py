from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet
from .models import (
    Question, Answer, Idea, Vocabulary, Topic
)
from .serializers import (
    Part3QuestionSerializer, Part3TopicSerializer, Part3IdeaSerializer, Part3VocabularySerializer,
    Part3AnswerSerializer,
)


class Part3QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Part3QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]


class Part3AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = Part3AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class Part3IdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = Part3IdeaSerializer
    permission_classes = [permissions.IsAuthenticated]


class Part3VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = Part3VocabularySerializer
    permission_classes = [permissions.IsAuthenticated]


class Part3TopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'part_3_questions__part_3_answers',
        'part_3_questions__part_3_ideas',
        'part_3_questions__part_3_vocabularies'
    )
    serializer_class = Part3TopicSerializer
    permission_classes = [permissions.IsAuthenticated]
