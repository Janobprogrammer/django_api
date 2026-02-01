from rest_framework.routers import DefaultRouter
from .views import (
    Part1TopicViewSet, Part1QuestionViewSet, Part1AnswerViewSet, Part1IdeaViewSet,
    Part1VocabularyViewSet,
)

router = DefaultRouter()
router.register('questions', Part1QuestionViewSet)
router.register('answers', Part1AnswerViewSet)
router.register('ideas', Part1IdeaViewSet)
router.register('vocabularies', Part1VocabularyViewSet)
router.register("topics", Part1TopicViewSet, basename="speaking-topics")

urlpatterns = router.urls