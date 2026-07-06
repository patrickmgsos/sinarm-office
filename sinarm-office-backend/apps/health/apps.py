"""Health app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class HealthConfig(AppConfig):
    """Configuration for operational health endpoints."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.health"
