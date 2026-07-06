"""Organization app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    """Configuration for organization infrastructure."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.organization"
