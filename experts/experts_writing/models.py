from django.db import models

TASK_CHOICES = (
    ('task1', 'Task 1'),
    ('task2', 'Task 2'),
)


class WritingTask(models.Model):
    task_type = models.CharField(max_length=5, choices=TASK_CHOICES)
    topic = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/writing/', null=True, blank=True)


class WritingEssay(models.Model):
    task = models.ForeignKey(WritingTask, on_delete=models.CASCADE, related_name='essays')
    text = models.TextField(null=True, blank=True)
    overall_band = models.FloatField()
    tr = models.FloatField()
    cc = models.FloatField()
    lr = models.FloatField()
    gra = models.FloatField()


class WritingFeedback(models.Model):
    essay = models.ForeignKey(WritingEssay, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.TextField(null=True, blank=True)
