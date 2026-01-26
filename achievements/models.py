from django.db import models


class UserAchievement(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    achieved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.title}"