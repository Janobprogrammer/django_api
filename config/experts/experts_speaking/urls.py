from rest_framework.routers import DefaultRouter
from .views import (
    SpeakingTopicViewSet,
    SpeakingQuestionViewSet,
    SpeakingAnswerViewSet,
    SpeakingIdeaViewSet,
    SpeakingVocabularyViewSet
)

router = DefaultRouter()
router.register('topics', SpeakingTopicViewSet)
router.register('questions', SpeakingQuestionViewSet)
router.register('answers', SpeakingAnswerViewSet)
router.register('ideas', SpeakingIdeaViewSet)
router.register('vocabularies', SpeakingVocabularyViewSet)

urlpatterns = router.urls
