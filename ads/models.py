from django.utils import timezone
from django.db import models


INTER_AD_CHOICES = (
    ("full", "FullScreen"),
    ("mini", "Mini"),
)


class InterAds(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, null=True)
    ad_type = models.CharField(choices=INTER_AD_CHOICES, max_length=255, blank=True, null=True)
    link = models.URLField(default="https://google.com/", blank=True, null=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    duration = models.PositiveIntegerField(default=10)
    views = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="static/inter_ad_images/", null=True, blank=True)

    class Meta:
        ordering = ("id",)

    def __str__(self):
        return f"{self.title}"
