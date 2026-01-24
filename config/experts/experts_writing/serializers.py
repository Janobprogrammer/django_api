from rest_framework import serializers
from .models import WritingFeedback, WritingEssay, WritingTask


class WritingFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = WritingFeedback
        fields = (
            'id',
            'text',
        )


class WritingEssaySerializer(serializers.ModelSerializer):
    feedbacks = WritingFeedbackSerializer(many=True, read_only=True)

    class Meta:
        model = WritingEssay
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


class WritingTaskSerializer(serializers.ModelSerializer):
    essays = WritingEssaySerializer(many=True, read_only=True)

    class Meta:
        model = WritingTask
        fields = (
            'id',
            'task_type',
            'topic',
            'image',
            'essays',
        )
