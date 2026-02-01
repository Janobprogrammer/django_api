from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Part2TopicViewSet,
    Part2QuestionViewSet,
    Part2AnswerViewSet,
    Part2IdeaViewSet,
    Part2VocabularyViewSet,
    Part2TopicNameViewSet
)

router = DefaultRouter()
router.register(r'topics', Part2TopicViewSet, basename='part2-topic')
router.register(r'questions', Part2QuestionViewSet, basename='part2-question')
router.register(r'answers', Part2AnswerViewSet, basename='part2-answer')
router.register(r'ideas', Part2IdeaViewSet, basename='part2-idea')
router.register(r'vocabularies', Part2VocabularyViewSet, basename='part2-vocabulary')
router.register(r'topic-names', Part2TopicNameViewSet, basename='part2-topicname')

urlpatterns = [
    path('', include(router.urls)),
]
