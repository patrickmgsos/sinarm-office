"""Production settings."""

from __future__ import annotations

from decouple import Csv, config
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F403

DEBUG = False
SECRET_KEY = config("SECRET_KEY")
if not SECRET_KEY:
    msg = "SECRET_KEY must be configured in production."
    raise ImproperlyConfigured(msg)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = config_bool("SESSION_COOKIE_SECURE", default=True)  # noqa: F405
CSRF_COOKIE_SECURE = config_bool("CSRF_COOKIE_SECURE", default=True)  # noqa: F405
SECURE_SSL_REDIRECT = config_bool("SECURE_SSL_REDIRECT", default=True)  # noqa: F405
