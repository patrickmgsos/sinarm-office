"""IA app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class IaConfig(AppConfig):
    """Configuration for the IA app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.ia"
