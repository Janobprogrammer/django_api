from rest_framework.routers import DefaultRouter
from .views import (
    TaskViewSet,
    EssayViewSet,
    FeedbackViewSet
)

router = DefaultRouter()
router.register('tasks', TaskViewSet)
router.register('essays', EssayViewSet)
router.register('feedbacks', FeedbackViewSet)

urlpatterns = router.urls
