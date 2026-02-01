from rest_framework.routers import DefaultRouter
from .views import (
    Part3TopicViewSet, Part3QuestionViewSet, Part3AnswerViewSet, Part3IdeaViewSet,
    Part3VocabularyViewSet,
)

router = DefaultRouter()
router.register('questions', Part3QuestionViewSet)
router.register('answers', Part3AnswerViewSet)
router.register('ideas', Part3IdeaViewSet)
router.register('vocabularies', Part3VocabularyViewSet)
router.register("topics", Part3TopicViewSet, basename="speaking-topics")

urlpatterns = router.urls