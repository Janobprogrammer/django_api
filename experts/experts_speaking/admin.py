from django.contrib import admin
from django.contrib.auth import get_user_model
from .forms import TopicAdminForm
from .models import (
    Idea, Answer, Question, Vocabulary, Topic,
)

User = get_user_model()

admin.site.register(Question)
admin.site.register(Idea)
admin.site.register(Vocabulary)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm

    class Media:
        js = ("js/speaking_part.js",)

    fields = ["title", "part", "topic_type", "main_question"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "teacher":
            kwargs["queryset"] = User.objects.filter(role="teacher")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# @admin.register(SpeakingPartName)
# class SpeakingPartNameAdmin(admin.ModelAdmin):
#
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "part_name":
#             kwargs["queryset"] = Topic.objects.filter(part="part2")
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

