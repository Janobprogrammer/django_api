from rest_framework import serializers
from .models import Feedback, Essay, Task


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'id',
            'text',
        )


class EssaySerializer(serializers.ModelSerializer):
    feedbacks = FeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = Essay
        fields = (
            'id',
            'text',
            'overall_band',
            'tr',
            'cc',
            'lr',
            'gra',
            'feedbacks',
        )


class TaskSerializer(serializers.ModelSerializer):
    essays = EssaySerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = (
            'id',
            'task_type',
            'topic',
            'image',
            'essays',
        )
