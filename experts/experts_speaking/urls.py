from rest_framework.routers import DefaultRouter
from .views import (
    SpeakingTopicViewSet,
    SpeakingQuestionViewSet,
    SpeakingAnswerViewSet,
    SpeakingIdeaViewSet,
    SpeakingVocabularyViewSet, SpeakingPart1ViewSet, SpeakingPart2ViewSet, SpeakingPart3ViewSet,
)

router = DefaultRouter()
# router.register('topics', SpeakingTopicViewSet)
router.register('questions', SpeakingQuestionViewSet)
router.register('answers', SpeakingAnswerViewSet)
router.register('ideas', SpeakingIdeaViewSet)
router.register('vocabularies', SpeakingVocabularyViewSet)
router.register("speaking/topics", SpeakingTopicViewSet, basename="speaking-topics")
router.register("speaking/part1", SpeakingPart1ViewSet, basename="speaking-part1")
router.register("speaking/part2", SpeakingPart2ViewSet, basename="speaking-part2")
router.register("speaking/part3", SpeakingPart3ViewSet, basename="speaking-part3")


urlpatterns = router.urls
