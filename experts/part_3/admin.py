from django.contrib import admin
from .forms import TopicAdminForm
from .models import (
    Topic, Question, Answer, Idea, Vocabulary, TopicType
)


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Idea)
admin.site.register(Vocabulary)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    form = TopicAdminForm
    list_display = ("title", "display_topic_type", "from_date", "to_date", "always_in_use")
    list_filter = ("topic_type", "always_in_use")
    search_fields = ("title",)
    filter_horizontal = ("topic_type",)

    def display_topic_type(self, obj):
        return ", ".join([t.name for t in obj.topic_type.all()])
    display_topic_type.short_description = "Topic Types"


@admin.register(TopicType)
class TopicTypeAdmin(admin.ModelAdmin):
    list_display = ("name", )