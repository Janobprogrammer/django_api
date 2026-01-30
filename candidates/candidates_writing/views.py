from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Task, Essay, Feedback
from .serializers import (
    TaskSerializer,
    EssaySerializer,
    FeedbackSerializer
)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.prefetch_related('essays__feedbacks')
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        task_type = self.request.query_params.get('task_type')
        if task_type:
            queryset = queryset.filter(task_type=task_type)
        return queryset


class EssayViewSet(ModelViewSet):
    queryset = Essay.objects.prefetch_related('feedbacks')
    serializer_class = EssaySerializer
    permission_classes = [IsAuthenticated]


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]
