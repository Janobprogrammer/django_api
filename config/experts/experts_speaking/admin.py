from django.contrib import admin
from .models import (
    SpeakingIdea, SpeakingAnswer, SpeakingQuestion, SpeakingVocabulary, SpeakingTopic
)


admin.site.register(SpeakingQuestion)
admin.site.register(SpeakingIdea)
admin.site.register(SpeakingAnswer)
admin.site.register(SpeakingVocabulary)
admin.site.register(SpeakingTopic)
