"""Core app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Configuration for cross-cutting backend foundations."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
