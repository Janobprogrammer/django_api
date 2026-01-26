from django.db import models


class Steak(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="steaks"
    )
    date = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} -> {self.date}"