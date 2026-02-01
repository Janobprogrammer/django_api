from django import forms
from .models import Topic


class TopicAdminForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        always_in_use = cleaned_data.get("always_in_use")
        if always_in_use:
            cleaned_data["from_date"] = None
            cleaned_data["to_date"] = None
        return cleaned_data