from django.db import models

PLAN_CHOICES = (
    ("default", "Default"),
    ("1_month", "1 Month"),
    ("3_month", "3 Month"),
    ("12_month", "12 Month"),
)


class SubscriptionHistory(models.Model):
    student = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    teacher = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="students"
    )
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default="default")

    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student} -> {self.teacher}"