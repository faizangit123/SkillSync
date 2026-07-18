from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    MeView,
    ChangePasswordView,
    UserStatsView,
    UserDetailView,
    AvatarUploadView,
)

urlpatterns = [
    # -------------------------
    # AUTH
    # -------------------------
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

    # -------------------------
    # USER (ME)
    # -------------------------
    path("me/", MeView.as_view(), name="me"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("stats/", UserStatsView.as_view(), name="user-stats-me"),

    # -------------------------
    # USER BY ID
    # -------------------------
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("<int:pk>/change-password/", ChangePasswordView.as_view(), name="change-password-id"),
    path("<int:pk>/avatar/", AvatarUploadView.as_view(), name="avatar-upload"),
    path("<int:pk>/stats/", UserStatsView.as_view(), name="user-stats-id"),

]
