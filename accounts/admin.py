from django.contrib import admin
from .models import User, PasswordResetOTP, PasswordResetOTPHistory

admin.site.register(User)


@admin.register(PasswordResetOTP)
class PasswordResetOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "created_at")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)


@admin.register(PasswordResetOTPHistory)
class PasswordResetOTPAdmin(admin.ModelAdmin):
    list_display = ("user", "code", "created_at")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)
