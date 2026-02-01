from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import (
    Topic, Question, Answer, Idea, Vocabulary,
)
from .serializers import (
    SpeakingTopicSerializer,
    SpeakingQuestionSerializer,
    SpeakingAnswerSerializer,
    SpeakingIdeaSerializer,
    SpeakingVocabularySerializer,
)


class SpeakingTopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'questions__answers',
        'questions__ideas',
        'questions__vocabularies'
    )
    serializer_class = SpeakingTopicSerializer
    permission_classes = [IsAuthenticated]


class SpeakingQuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = SpeakingQuestionSerializer
    permission_classes = [IsAuthenticated]


class SpeakingAnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = SpeakingAnswerSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]


class SpeakingIdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = SpeakingIdeaSerializer
    permission_classes = [IsAuthenticated]


class SpeakingVocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = SpeakingVocabularySerializer
    permission_classes = [IsAuthenticated]


class SpeakingPart1ViewSet(ModelViewSet):
    serializer_class = SpeakingTopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Topic.objects.filter(part="part1")


class SpeakingPart2ViewSet(ModelViewSet):
    serializer_class = SpeakingTopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Topic.objects.filter(part="part2")


class SpeakingPart3ViewSet(ModelViewSet):
    serializer_class = SpeakingTopicSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Topic.objects.filter(part="part3")

