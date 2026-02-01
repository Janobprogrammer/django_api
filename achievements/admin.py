from django.contrib import admin
from .models import Achievement, UserAchievedAt


admin.site.register(UserAchievedAt)
admin.site.register(Achievement)

