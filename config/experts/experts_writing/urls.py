from rest_framework.routers import DefaultRouter
from .views import (
    WritingTaskViewSet,
    WritingEssayViewSet,
    WritingFeedbackViewSet
)

router = DefaultRouter()
router.register('tasks', WritingTaskViewSet)
router.register('essays', WritingEssayViewSet)
router.register('feedbacks', WritingFeedbackViewSet)

urlpatterns = router.urls
