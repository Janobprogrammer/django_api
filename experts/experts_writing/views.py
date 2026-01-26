from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import WritingTask, WritingEssay, WritingFeedback
from .serializers import (
    WritingTaskSerializer,
    WritingEssaySerializer,
    WritingFeedbackSerializer
)


class WritingTaskViewSet(ModelViewSet):
    queryset = WritingTask.objects.prefetch_related('essays__feedbacks')
    serializer_class = WritingTaskSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = super().get_queryset()
        task_type = self.request.query_params.get('task_type')
        if task_type:
            queryset = queryset.filter(task_type=task_type)
        return queryset


class WritingEssayViewSet(ModelViewSet):
    queryset = WritingEssay.objects.prefetch_related('feedbacks')
    serializer_class = WritingEssaySerializer
    permission_classes = [AllowAny]


class WritingFeedbackViewSet(ModelViewSet):
    queryset = WritingFeedback.objects.all()
    serializer_class = WritingFeedbackSerializer
    permission_classes = [AllowAny]



