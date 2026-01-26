from django.db import models
from django.core.exceptions import ValidationError


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

    class Meta:
        unique_together = ("user", "friend")

    def clean(self):
        if self.user == self.friend:
            raise ValidationError("User cannot add himself as a friend !!!")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
