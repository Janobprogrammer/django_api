from django.contrib import admin
from .models import WritingFeedback, WritingTask, WritingEssay


admin.site.register(WritingTask)
admin.site.register(WritingFeedback)
admin.site.register(WritingEssay)
