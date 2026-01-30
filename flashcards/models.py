from django.db import models


FLASH_CARD_CHOICES = (
    ("general", "General"),
    ("academic", "Academic"),
)

class FlashCard(models.Model):
    author = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="flashcards"
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    flash_type = models.CharField(max_length=255, choices=FLASH_CARD_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.author} -> {self.title}"


class WordList(models.Model):
    flash_card = models.ForeignKey("FlashCard", on_delete=models.CASCADE, related_name="flash_cards")
    word = models.CharField(max_length=255, null=True, blank=True)
    definition = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="static/flash_cards_images/", blank=True, null=True)

    def __str__(self):
        return f"{self.word}"