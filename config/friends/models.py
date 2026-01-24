from django.db import models


class FriendList(models.Model):
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="user"
    )
    friend = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="friends"
    )

    def __str__(self):
        return f"{self.user} -> {self.friend}"
