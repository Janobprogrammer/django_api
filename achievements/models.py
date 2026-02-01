from django.db import models


TYPES = (
    ("weekly", "Weekly"),
    ("monthly", "Monthly"),
    ("yearly", "Yearly"),
)

class Achievement(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    achievement_type = models.CharField(max_length=255, choices=TYPES, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    max_quantity = models.PositiveIntegerField(default=0)
    icon = models.ImageField(upload_to="achievements/images", null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.title}"


class UserAchievedAt(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="achieved_user")
    achievement = models.ForeignKey("Achievement", on_delete=models.CASCADE, related_name="achievements")
    quantity = models.PositiveIntegerField(default=0)
    achievements_date = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return f"{self.achievement}"