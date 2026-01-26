from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import timedelta
from subscriptions.models import SubscriptionHistory
from .models import Follow

PLAN_TO_DAYS = {
    "default": 0,
    "1_month": 30,
    "3_month": 90,
    "12_month": 365,
}


@receiver(post_save, sender=Follow)
def create_subscription_history(sender, instance, created, **kwargs):
    if not created:
        return

    start_date = timezone.now().date()

    plan = getattr(instance, "plan", "default")
    days = PLAN_TO_DAYS.get(plan, 30)

    end_date = start_date + timedelta(days=days)

    SubscriptionHistory.objects.create(
        student=instance.follower,
        teacher=instance.following,
        plan=plan,
        start_date=start_date,
        end_date=end_date
    )
