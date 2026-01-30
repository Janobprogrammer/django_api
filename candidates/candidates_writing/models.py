from django.db import models

TASK_CHOICES = (
    ('task1', 'Task 1'),
    ('task2', 'Task 2'),
)


class Task(models.Model):
    task_type = models.CharField(max_length=5, choices=TASK_CHOICES)
    topic = models.CharField(max_length=255)
    image = models.ImageField(upload_to='writing/images', null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.topic}"


class Essay(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='essays')
    text = models.TextField(null=True, blank=True)
    overall_band = models.FloatField()
    tr = models.FloatField()
    cc = models.FloatField()
    lr = models.FloatField()
    gra = models.FloatField()

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.task}"


class Feedback(models.Model):
    essay = models.ForeignKey(Essay, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.essay}"
