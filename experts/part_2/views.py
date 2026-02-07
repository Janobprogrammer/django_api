from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Topic, Question, Answer, Idea, Vocabulary, TopicName
from .serializers import (
    Part2TopicSerializer,
    Part2QuestionSerializer,
    Part2AnswerSerializer,
    Part2IdeaSerializer,
    Part2VocabularySerializer,
    Part2TopicNameSerializer
)


class Part2TopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'part_2_answers',
        'part_2_ideas',
        'part_2_vocabularies',
    )
    serializer_class = Part2TopicSerializer
    permission_classes = [IsAuthenticated]


class Part2QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = Part2QuestionSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class Part2AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = Part2AnswerSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class Part2IdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = Part2IdeaSerializer
    permission_classes = [IsAuthenticated]


class Part2VocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = Part2VocabularySerializer
    permission_classes = [IsAuthenticated]


class Part2TopicNameViewSet(ModelViewSet):
    queryset = TopicName.objects.all()
    serializer_class = Part2TopicNameSerializer
    permission_classes = [IsAuthenticated]
