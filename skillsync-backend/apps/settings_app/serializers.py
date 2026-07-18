from rest_framework import serializers
from .models import NotificationSettings, UserSettings

class NotificationSettingsSerializer(serializers.ModelSerializer):
    emailNotifications = serializers.BooleanField(source='email_notifications', required=False)
    pushNotifications = serializers.BooleanField(source='push_notifications', required=False)
    weeklyDigest = serializers.BooleanField(source='weekly_digest', required=False)
    projectUpdates = serializers.BooleanField(source='project_updates', required=False)
    skillReminders = serializers.BooleanField(source='skill_reminders', required=False)

    class Meta:
        model = NotificationSettings
        fields = (
            'emailNotifications',
            'pushNotifications',
            'weeklyDigest',
            'projectUpdates',
            'skillReminders',
        )

class UserSettingsSerializer(serializers.ModelSerializer):
    twoFactorEnabled = serializers.BooleanField(source='two_factor_enabled', required=False)

    class Meta:
        model = UserSettings
        fields = (
            'language',
            'timezone',
            'theme',
            'twoFactorEnabled',
        )
