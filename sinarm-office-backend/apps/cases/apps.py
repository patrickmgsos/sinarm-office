"""Case MVP app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class CasesConfig(AppConfig):
    """Configuration for the Case MVP domain."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cases"
    verbose_name = "Cases"
