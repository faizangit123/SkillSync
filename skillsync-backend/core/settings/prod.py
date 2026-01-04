from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# ===============================
# CORS (PRODUCTION)
# ===============================
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend.onrender.com",  # change this
]
