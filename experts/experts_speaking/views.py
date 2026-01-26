from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import (
    Topic,
    TopicQuestion,
    Answer,
    Idea,
    Vocabulary,
    SpeakingExam,
)
from .serializers import (
    SpeakingTopicSerializer,
    SpeakingQuestionSerializer,
    SpeakingAnswerSerializer,
    SpeakingIdeaSerializer,
    SpeakingVocabularySerializer,
    SpeakingExamSerializer,
    SpeakingExamWriteSerializer,
)


class SpeakingTopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'questions__answers',
        'questions__ideas',
        'questions__vocabularies'
    )
    serializer_class = SpeakingTopicSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        part = self.request.query_params.get('part')
        if part:
            queryset = queryset.filter(part=part)
        return queryset


class SpeakingQuestionViewSet(ModelViewSet):
    queryset = TopicQuestion.objects.all()
    serializer_class = SpeakingQuestionSerializer
    permission_classes = [AllowAny]


class SpeakingAnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = SpeakingAnswerSerializer
    permission_classes = [AllowAny]


class SpeakingIdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = SpeakingIdeaSerializer
    permission_classes = [AllowAny]


class SpeakingVocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = SpeakingVocabularySerializer
    permission_classes = [AllowAny]


class SpeakingExamViewSet(ModelViewSet):
    queryset = SpeakingExam.objects.select_related(
        'part1',
        'part2',
        'part3',
    ).prefetch_related(
        'part1__questions__answers',
        'part1__questions__ideas',
        'part1__questions__vocabularies',

        'part2__questions__answers',
        'part2__questions__ideas',
        'part2__questions__vocabularies',

        'part3__questions__answers',
        'part3__questions__ideas',
        'part3__questions__vocabularies',
    )

    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SpeakingExamWriteSerializer
        return SpeakingExamSerializer
