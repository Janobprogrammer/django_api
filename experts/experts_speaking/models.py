from django.db import models


TOPIC_CHOICES = (
    ('old', 'Old'),
    ('new', 'New'),
    ('free', 'Free'),
    ('paid', 'Paid'),
    ('archived', 'Archived'),
)
PART_CHOICES = (
    ('part1', 'Part 1'),
    ('part2', 'Part 2'),
    ('part3', 'Part 3'),
)


class Topic(models.Model):
    title = models.CharField(max_length=255)
    topic_type = models.CharField(max_length=100, choices=TOPIC_CHOICES)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.title}"


class SpeakingPart(models.Model):
    title = models.CharField(max_length=255)
    part = models.CharField(max_length=5, choices=PART_CHOICES)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name='speaking_topic'
    )
    main_question = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.part} - {self.title}"


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.question


class Answer(models.Model):
    teacher = models.ForeignKey("accounts.User", on_delete=models.CASCADE, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(null=True, blank=True)
    audio = models.FileField(upload_to='speaking/audio/', null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.teacher}"


class Idea(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='ideas')
    idea = models.CharField(max_length=255)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.idea}"


class Vocabulary(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='vocabularies')
    word = models.CharField(max_length=100)
    definition = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.word}"


class SpeakingExam(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    part1 = models.ForeignKey(
        SpeakingPart,
        on_delete=models.CASCADE,
        related_name='exam_part1',
        limit_choices_to={'part': 'part1'}
    )

    part2 = models.ForeignKey(
        SpeakingPart,
        on_delete=models.CASCADE,
        related_name='exam_part2',
        limit_choices_to={'part': 'part2'}
    )

    part3 = models.ForeignKey(
        SpeakingPart,
        on_delete=models.CASCADE,
        related_name='exam_part3',
        limit_choices_to={'part': 'part3'}
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.name


class SpeakingPartName(models.Model):
    part_name = models.ForeignKey("SpeakingPart", on_delete=models.CASCADE, related_name="part_names")
    topic_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return self.topic_name

