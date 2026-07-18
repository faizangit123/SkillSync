from django.urls import path
from .views import (
    NotificationSettingsView,
    UserSettingsView,
    EnableTwoFactorView,
    DisableTwoFactorView,
    ExportUserDataView,
)

urlpatterns = [
    path("", UserSettingsView.as_view()),
    path("notifications/", NotificationSettingsView.as_view()),
    path("2fa/enable/", EnableTwoFactorView.as_view()),
    path("2fa/disable/", DisableTwoFactorView.as_view()),
    path("export/", ExportUserDataView.as_view()),
]
