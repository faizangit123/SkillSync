from django.contrib import admin
from django.urls import path, include
from .views import health_check  # ✅ add this

urlpatterns = [
    path("admin/", admin.site.urls),

    # Health check (Render)
    path("healthz", health_check),  # ✅ add this

    # Auth
    path("api/auth/", include("apps.users.urls")),

    # Users
    path("api/users/", include("apps.users.urls")),

    # Core APIs
    path("api/skills/", include("apps.skills.urls")),
    path("api/projects/", include("apps.projects.urls")),
    path("api/notifications/", include("apps.notifications.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
]
