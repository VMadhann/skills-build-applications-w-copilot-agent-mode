import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "octofit-development-key")
DEBUG = os.environ.get("DJANGO_DEBUG", "1") == "1"
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("CODESPACE_NAME"):
    ALLOWED_HOSTS.append(f"{os.environ['CODESPACE_NAME']}-8000.app.github.dev")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "octofit_tracker.tracker",
]
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]
ROOT_URLCONF = "octofit_tracker.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": [
            "django.template.context_processors.request",
            "django.contrib.auth.context_processors.auth",
            "django.contrib.messages.context_processors.messages",
        ]},
    }
]
USE_TZ = True
DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]
CORS_ALLOW_HEADERS = ["accept", "authorization", "content-type", "user-agent", "x-csrftoken", "x-requested-with"]
STATIC_URL = "static/"

if os.environ.get("MONGODB_URI"):
    DATABASES = {
        "default": {
            "ENGINE": "djongo",
            "NAME": os.environ.get("MONGODB_NAME", "octofit_db"),
            "ENFORCE_SCHEMA": False,
            "CLIENT": {"host": os.environ["MONGODB_URI"]},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "octofit.sqlite3",
        }
    }