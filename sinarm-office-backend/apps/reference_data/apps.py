"""Reference data app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class ReferenceDataConfig(AppConfig):
    """Configuration for technical reference data."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.reference_data"
