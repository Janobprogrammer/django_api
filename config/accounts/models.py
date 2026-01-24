import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager
import hashlib
from django.conf import settings

ROLE_CHOICES = (
    ("user", "User"),
    ("teacher", "Teacher"),
    ("admin", "Admin"),
    ("superadmin", "Super Admin"),
)
GENDER_CHOICES = (
    ("male", "Male"),
    ("female", "Female"),
)
PLAN_CHOICES = (
    ("default", "Default"),
    ("1_month", "1 Month"),
    ("3_month", "3 Month"),
    ("12_month", "12 Month"),
)


def generate_public_id(email: str) -> str | None:
    if len(email) < 8:
        return None
    if "@" not in email:
        return None
    base = email.split("@")[0].lower()
    salt = settings.SECRET_KEY
    rnd = random.randint(1000, 9999)

    raw = f"{base}{rnd}{salt}"
    return hashlib.sha256(raw.encode()).hexdigest()[:8]


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    uuid = models.CharField(
        unique=True, blank=True, null=True, max_length=20,
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100, blank=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user"
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES,
        null=True,
        blank=True
    )

    avatar = models.ImageField(
        upload_to="static/avatars/",
        null=True,
        blank=True,
    )

    phone_model = models.CharField(max_length=255, blank=True)

    # --------- SOCIAL ---------
    instagram = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    youtube = models.URLField(blank=True)

    # --------- IELTS SCORES ---------
    speaking_band = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reading_band = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    listening_band = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    writing_band = models.DecimalField(max_digits=3, decimal_places=1, default=0)

    trf_number = models.CharField(max_length=100, blank=True)
    trf_date = models.DateField(null=True, blank=True)

    # --------- SYSTEM ---------
    balance = models.PositiveIntegerField(default=0)   # inter coin
    points = models.PositiveIntegerField(default=0)

    steaks_count = models.PositiveIntegerField(default=0)

    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    rating_count = models.PositiveIntegerField(default=0)
    reward = models.PositiveIntegerField(default=5, help_text="InterCoin reward for this user added via referral.")
    likes = models.PositiveIntegerField(default=0, editable=False)

    last_active = models.DateTimeField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    premium = models.CharField(max_length=255, default="default", choices=PLAN_CHOICES)

    # --------- FRIEND SYSTEM ---------
    user_uuid = models.CharField(
        max_length=8,
        unique=True,
        db_index=True
    )

    # --------- CONFIG ---------
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["uuid"]

    class Meta:
        ordering = ["-date_joined"]

    def save(self, *args, **kwargs):
        if not self.user_uuid:
            for _ in range(5):
                code = generate_public_id(self.email)
                if code is None:
                    continue
                if not User.objects.filter(user_uuid=code).exists():
                    self.user_uuid = code
                    break
        self.user_uuid = str(self.user_uuid).upper()
        self.uuid = str(self.uuid).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
