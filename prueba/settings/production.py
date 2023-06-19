import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "RENDER" not in os.environ

if not DEBUG:
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ALLOWED_HOSTS = ["*"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=f"postgresql://{os.environ.get('USER_FRACTTAL')}:{os.environ.get('PASSWORD_FRACTTAL')}@{os.environ.get('HOST_FRACTTAL')}:{os.environ.get('PORT_FRACTTAL')}/{os.environ.get('NAME_FRACTTAL')}",
        conn_max_age=1000,
    )
}
