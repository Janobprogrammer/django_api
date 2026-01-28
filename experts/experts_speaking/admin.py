from django.contrib import admin
from .models import (
    Idea, Answer, TopicQuestion, Vocabulary, Topic, SpeakingExam, SpeakingPart
)


admin.site.register(TopicQuestion)
admin.site.register(Idea)
admin.site.register(Answer)
admin.site.register(Vocabulary)
admin.site.register(Topic)
admin.site.register(SpeakingExam)
admin.site.register(SpeakingPart)
