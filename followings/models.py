from django.db import models


PLAN_CHOICES = (
    ("default", "Default"),
    ("1_month", "1 Month"),
    ("3_month", "3 Month"),
    ("12_month", "12 Month"),
)


class Follow(models.Model):
    follower = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="followers")
    following = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="following")
    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.follower} -> {self.following}"
    
    def save(self, *args, **kwargs):
        if self.follower == self.following:
            return
        super().save(*args, **kwargs)
