"""Configuration app setup."""

from __future__ import annotations

from django.apps import AppConfig


class ConfigurationConfig(AppConfig):
    """Configuration for runtime settings infrastructure."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.configuration"
