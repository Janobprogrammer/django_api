from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

TOPIC_CHOICES = (
    ('old', 'Old'),
    ('new', 'New'),
    ('free', 'Free'),
    ('paid', 'Paid'),
    ('archived', 'Archived'),
    ('common', 'Common'),
    ('not_confirmed_yet', 'Not confirmed yet'),
)
PART_CHOICES = (
    ('part1', 'Part 1'),
    ('part2', 'Part 2'),
    ('part3', 'Part 3'),
)


class TopicType(models.Model):
    name = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    def __str__(self):
        return self.name


class Topic(models.Model):
    title = models.CharField(max_length=255)
    topic_type = models.ManyToManyField("TopicType", blank=True)
    question = models.CharField(max_length=500, )
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    always_in_use = models.BooleanField(default=False)

    class Meta:
        ordering = ("id",)

    def clean(self):
        if self.from_date:
            self.from_date = self.from_date.replace(day=1)
        if self.to_date:
            self.to_date = self.to_date.replace(day=1)

        if self.from_date and self.to_date and self.from_date > self.to_date:
            raise ValidationError("from_date to_date dan keyin bo‘la olmaydi")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.question}"


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='part_2_questions')
    question = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='speaking/audio/', null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.question


class Answer(models.Model):
    teacher = models.ForeignKey("accounts.User", on_delete=models.CASCADE, default=None, related_name='part_2_answered_teacher')
    question = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='part_2_answers')
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='speaking/audio/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.teacher}"


class Idea(models.Model):
    question = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='part_2_ideas')
    idea = models.CharField(max_length=255)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.idea}"


class Vocabulary(models.Model):
    question = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='part_2_vocabularies')
    word = models.CharField(max_length=100)
    definition = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.word}"


class TopicName(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="part_2_names")
    part3_name = models.ForeignKey("part_3.Topic", on_delete=models.CASCADE, related_name="part3_names")

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.part3_name}"
