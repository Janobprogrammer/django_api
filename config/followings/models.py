from django.db import models


class Follow(models.Model):
    follower = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="following"
    )
    following = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="followers"
    )

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower} -> {self.following}"

