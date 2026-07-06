"""Identity app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class IdentityConfig(AppConfig):
    """Configuration for reusable identity infrastructure."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.identity"
