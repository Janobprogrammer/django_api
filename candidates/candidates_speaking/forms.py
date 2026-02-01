from django import forms
from .models import SpeakingPart


class SpeakingPartAdminForm(forms.ModelForm):
    class Meta:
        model = SpeakingPart
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        part = cleaned_data.get("part")
        main_question = cleaned_data.get("main_question")

        if part == "part2" and not main_question:
            raise forms.ValidationError(
                "Part 2 bo‘lsa, main_question majburiy!"
            )

        if part != "part2":
            cleaned_data["main_question"] = None

        return cleaned_data