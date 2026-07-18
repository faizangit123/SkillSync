from django.db import models
from django.conf import settings

class NotificationSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notification_settings"
    )
    email_notifications = models.BooleanField(default=True)
    push_notifications = models.BooleanField(default=True)
    weekly_digest = models.BooleanField(default=True)
    project_updates = models.BooleanField(default=True)
    skill_reminders = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification Settings for {self.user.email}"

class UserSettings(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_settings"
    )
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("es", "Spanish"),
        ("fr", "French"),
        ("de", "German"),
    ]
    THEME_CHOICES = [
        ("light", "Light"),
        ("dark", "Dark"),
        ("system", "System"),
    ]
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default="en")
    timezone = models.CharField(max_length=50, default="UTC")
    theme = models.CharField(max_length=10, choices=THEME_CHOICES, default="system")
    two_factor_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"User Settings for {self.user.email}"
