from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import SpeakingPartAdminForm
from .models import (
    Idea, Answer, Question, Vocabulary, Topic, SpeakingExam, SpeakingPart, SpeakingPartName,
)

User = get_user_model()

admin.site.register(Question)
admin.site.register(Idea)
admin.site.register(Vocabulary)
admin.site.register(Topic)
admin.site.register(SpeakingExam)


@admin.register(SpeakingPart)
class SpeakingPartAdmin(admin.ModelAdmin):
    form = SpeakingPartAdminForm

    class Media:
        js = ("js/speaking_part.js",)

    fields = ["title", "part", "topic", "main_question"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(role="teacher")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(SpeakingPartName)
class SpeakingPartNameAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "part_name":
            kwargs["queryset"] = SpeakingPart.objects.filter(part="part2")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

