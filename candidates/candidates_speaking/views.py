from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import (
    Topic, Question, Answer, Idea, Vocabulary, SpeakingExam,
)
from .serializers import (
    TopicSerializer,
    PartSerializer,
    QuestionSerializer,
    CandidatesAnswerSerializer,
    IdeaSerializer,
    VocabularySerializer,
    ExamSerializer,
    ExamWriteSerializer,
)


class SpeakingTopicViewSet(ModelViewSet):
    queryset = Topic.objects.prefetch_related(
        'questions__answers',
        'questions__ideas',
        'questions__vocabularies'
    )
    serializer_class = TopicSerializer
    permission_classes = [IsAuthenticated]


class SpeakingQuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]


class SpeakingAnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = CandidatesAnswerSerializer
    permission_classes = [IsAuthenticated]


class SpeakingIdeaViewSet(ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]


class SpeakingVocabularyViewSet(ModelViewSet):
    queryset = Vocabulary.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = [IsAuthenticated]


class SpeakingExamViewSet(ModelViewSet):
    queryset = SpeakingExam.objects.select_related(
        'part1',
        'part2',
        'part3',
    ).prefetch_related(
        'part1__topic__questions__answers',
        'part1__topic__questions__ideas',
        'part1__topic__questions__vocabularies',

        'part2__topic__questions__answers',
        'part2__topic__questions__ideas',
        'part2__topic__questions__vocabularies',
        'part2__part_names',

        'part3__topic__questions__answers',
        'part3__topic__questions__ideas',
        'part3__topic__questions__vocabularies',
    )

    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ExamWriteSerializer
        return ExamSerializer
